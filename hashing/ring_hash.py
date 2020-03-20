#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
"""
pure implementation of consistent hash based on ring hash
https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
https://medium.com/@dgryski/consistent-hashing-algorithmic-tradeoffs-ef6b8e2fcae8
https://www.akamai.com/es/es/multimedia/documents/technical-publication/consistent-hashing-and-random-trees-distributed-caching-protocols-for-relieving-hot-spots-on-the-world-wide-web-technical-publication.pdf
"""

from murmur3 import murmur3_hash

# Amount of points on the ring. Must not be higher than 2**32 because we're
# using murmur3 for hash
RING_SIZE = 2 ** 32

# Default amount of replicas per node
RING_REPLICAS = 16


class RingHash(object):
    """
    The basic idea is that each server is mapped to a point on
    a circle (You can think of the circle as all integers 0 ..2³²-1.)
    with a hash function. To lookup the server for a given key, you hash
    the key and find that point on the circle.
    Then you scan forward until you find the first hash value for any server.
    In practice, each server appears multiple times on the circle. \
    These extra points are called “virtual nodes”, or “vnodes”  or replicas.
    """

    def __init__(self, replicas_count=None, get_hash=None):
        if replicas_count is None:
            replicas_count = RING_REPLICAS
        self.replicas = replicas_count
        self._hashMap = {}
        self._ring_hash = []
        self._nodes = {}
        if get_hash is None:
            get_hash = murmur3_hash
        self.get_hash = get_hash

    @property
    def Nodes(self):
        return self._nodes.values

    def _GetReplicasHashes(self, node):
        _hashes = []
        for num in range(0, self.replicas):
            _hash = self.get_hash(str(node) + " " + str(num))
            _hashes.append(_hash)
        return _hashes

    def _AddNode(self, node, node_hash, hashes):
        self._nodes[node_hash] = node
        for _hash in hashes:
            self._hashMap[_hash] = node_hash
            self._ring_hash.append(_hash)
        self._ring_hash.sort()

    def _GetNextShard(self, key_hash):
        '''Return next vnode for hash'''
        if not self._ring_hash:
            return None
        return next((x for x in self._ring_hash if x > key_hash), self._ring_hash[0])

    def _GetPrevShard(self, key_hash):
        ''' return previous vnode for hash
        '''
        if not self._ring_hash:
            return None
        r = [x for x in self._ring_hash if x < key_hash]
        if not r:
            return max(self._ring_hash)
        return max(r)

    def AddNode(self, nodes):
        '''
        Add new node(s) to ring hash

        Parameters:

        nodes: *list*|*string* - list of nodes or single node
        '''
        if not isinstance(nodes, list):
            return self.AddNode([nodes])
        for node in nodes:
            node_hash = self.get_hash(str(node))
            if node_hash not in self._nodes:
                _hashes = self._GetReplicasHashes(node)
                self._AddNode(node, node_hash, _hashes)

    def GetAffectedNodes(self, nodes):
        '''
        Return v-nodes hashes of which will be affected after added new hash
        '''
        if not isinstance(nodes, list):
            return self.GetAffectedNodes([nodes])
        shards = set()
        _hashes = [x for node in nodes for x in self._GetReplicasHashes(node)]
        for key_hash in _hashes:
            shard = self._GetNextShard(key_hash)
            if shard not in shards and shard is not None:
                shards.add(shard)
        return list(shards)

    def Get(self, key):
        key_hash = self.get_hash(key)
        shard = self._GetNextShard(key_hash)
        return shard

    def RemoveNode(self, node):
        node_hash = self.get_hash(str(node))
        if not self._nodes[node_hash]:
            return
        _hashes = self._GetReplicasHashes(node)
        if not _hashes:
            return []
        nodes = set()
        for _hash in _hashes:
            if _hash in self._hashMap:
                if _hash not in nodes:
                    node_hash = self._hashMap[_hash]
                    nodes.add(self._nodes[node_hash])
                    self._ring_hash.remove(_hash)
                    del self._hashMap[_hash]
                    del self._nodes[node_hash]
        return list(nodes)
