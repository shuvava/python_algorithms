#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
pure implementation of consistent hash based on ring hash
https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
https://medium.com/@dgryski/consistent-hashing-algorithmic-tradeoffs-ef6b8e2fcae8
https://www.akamai.com/es/es/multimedia/documents/technical-publication/consistent-hashing-and-random-trees-distributed-caching-protocols-for-relieving-hot-spots-on-the-world-wide-web-technical-publication.pdf
'''

from murmur3 import murmur3_hash

# Amount of points on the ring. Must not be higher than 2**32 because we're
# using murmur3 for hash
RING_SIZE = 2**32

# Default amount of replicas per node
RING_REPLICAS = 16

class RingHash(object):
    '''
    The basic idea is that each server is mapped to a point on
    a circle (You can think of the circle as all integers 0 ..2³²-1.)
    with a hash function. To lookup the server for a given key, you hash
    the key and find that point on the circle.
    Then you scan forward until you find the first hash value for any server.
    In practice, each server appears multiple times on the circle. 
    These extra points are called “virtual nodes”, or “vnodes”  or replicas.
    '''
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

    def _GetReplicasHashes(self, node, node_hash):
        _hashes = []
        for num in range(0, self.replicas):
            _hash = self.get_hash(str(node) + " " + num)
            _hashes.append(_hash)
        return _hashes

    def _AddNode(self, node, node_hash, hashes):
        self._nodes[node_hash] = node
        for _hash in hashes:
            self._hashMap[_hash] = (node, node_hash)
            self._ring_hash.append(_hash)

    def _GetNextShard(self, key_hash):
        return next((x for x in self._ring_hash if x > key_hash), self._ring_hash[0])

    def _GetPrevShard(self, key_hash):
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
            self.AddNode([nodes])
        _range = (0, RING_SIZE)
        for node in nodes:
            node_hash = self.get_hash(str(node))
            if not self._nodes[node_hash]:
                _hashes = self._GetReplicasHashes(node, node_hash)
                _range = (min(_range[0], self._GetPrevShard(min(_hashes))), max(_range[1], self._GetNextShard(max(_hashes))))
                self._AddNode(node, node_hash, _hashes)
        

        self._ring_hash = self._ring_hash.sort()
        return _range

    def Get(self, key):
        key_hash = self.get_hash(key)
        shard = self._GetNextShard(key_hash)
        return shard

    def RemoveNode(self, node):
        node_hash = self.get_hash(str(node))
        if not self._nodes[node_hash]:
            return None
        _range = (0, RING_SIZE)
        _hashes = self._GetReplicasHashes(node, node_hash)
        return _range
