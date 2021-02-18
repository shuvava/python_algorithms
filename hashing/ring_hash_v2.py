#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
#
"""
pure implementation of consistent hash based on ring hash
https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
https://medium.com/@dgryski/consistent-hashing-algorithmic-tradeoffs-ef6b8e2fcae8
https://www.akamai.com/es/es/multimedia/documents/technical-publication/consistent-hashing-and-random-trees-distributed-caching-protocols-for-relieving-hot-spots-on-the-world-wide-web-technical-publication.pdf
"""
from bisect import bisect
from enum import Enum
from hashlib import md5
from typing import List, Dict, Optional

# Default amount of replicas per node
RING_REPLICAS = 16
NODE_ID = 'node_id'
NODE_WGT = 'weight'
NODE_VN = 'v_nodes'


def _default_hash_fn(key) -> int:
    return int(md5(str(key).encode("utf-8")).hexdigest(), 16)


class RingObjectType(Enum):
    OBJ = 1
    ID = 2


class RingHash:
    """
    The basic idea is that each server is mapped to a point on
    a circle (You can think of the circle as all integers 0 ..2³²-1.)
    with a hash function. To lookup the server for a given key, you hash
    the key and find that point on the circle.
    Then you scan forward until you find the first hash value for any server.
    In practice, each server appears multiple times on the circle. \
    These extra points are called “virtual nodes”, or “vnodes”  or replicas.
    """

    def __init__(self, nodes=None, replicas_cnt=None, hash_fn=None):
        """
        create ring hash structure

        :param nodes: list is nodes ids/ configurations
        :param replicas_cnt: number of replicas/vNodes of each node
        :param hash_fn: a hash function

        Examples:
        >>> from hashing.ring_hash_v2 import RingHash
        >>> hash = RingHash([3, 6, 9], 1)
        >>> node_id = hash.get(3)
        """
        self._keys = []
        self._nodes = {}
        self._ring = {}

        if hash_fn and not hasattr(hash_fn, "__call__"):
            raise TypeError("hash_fn should be a callable function")
        self._hash_fn = hash_fn or _default_hash_fn
        self._default_replicas = replicas_cnt or RING_REPLICAS

        self.add(nodes)

    def _get_hash(self, node_name: str, w: int) -> int:
        key = f"{node_name}-{w}"
        return self._hash_fn(key)

    def _create_node(self, node) -> Dict[str, any]:
        if isinstance(node, str) or isinstance(node, int):
            node = {NODE_ID: node}
        elif not isinstance(node, dict):
            raise ValueError(
                f"node should be a string or a dict got {type(node)}"
            )
        if NODE_ID not in node:
            raise ValueError(
                f"'{NODE_ID}' property should be present in dict"
            )
        if NODE_WGT not in node:
            node[NODE_WGT] = 1
        elif not isinstance(node[NODE_WGT], int) or node[NODE_WGT] < 1:
            raise ValueError(
                f"node weight '{node[NODE_WGT]}' should be int and be grate than 0"
            )
        if NODE_VN not in node:
            node[NODE_VN] = self._default_replicas
        elif not isinstance(node[NODE_VN], int) or node[NODE_VN] < 1:
            raise ValueError(
                f"node replicas count '{node[NODE_VN]}' should be int and be grate than 0"
            )
        return node

    def _add_nodes(self, nodes: List[Dict[str, any]]):
        """add nodes into the ring"""
        _nodes = []
        for node in nodes:
            _node = self._create_node(node)
            if _node[NODE_ID] in self._nodes:
                raise ValueError(
                    f"node with the name {_node[NODE_ID]} already had been added"
                )
            _nodes.append(_node)

        for node in _nodes:
            node_id = node[NODE_ID]
            self._nodes[node_id] = node
            for w in range(0, node[NODE_VN] * node[NODE_WGT]):
                _hash = self._get_hash(node_id, w)
                self._ring[_hash] = node_id
        self._keys = sorted(self._ring.keys())

    def _get_node_id(self, node_id: str) -> str:
        """return node Id for given key"""
        _hash = self._hash_fn(node_id)
        inx = bisect(self._keys, _hash)
        if inx == len(self._keys):
            inx = 0
        return self._ring[self._keys[inx]]

    def remove(self, node_id: str) -> Dict[str, any]:
        """remove node from the ring"""
        if node_id not in self._nodes:
            raise ValueError(
                f"node with id '{node_id}' not found"
            )
        node: Dict[str, any] = self._nodes.pop(node_id)
        for w in range(0, node[NODE_VN] * node[NODE_WGT]):
            _hash = self._get_hash(node_id, w)
            del self._ring[_hash]
        self._keys = sorted(self._ring.keys())
        return node

    def get(self, key: str, res_type: Optional[RingObjectType] = None):
        """getting node for given key"""
        node_id = self._get_node_id(key)
        if res_type is None:
            res_type = RingObjectType.ID
        if res_type == RingObjectType.ID:
            return node_id
        node = self._nodes[node_id]
        return node

    def add(self, nodes):
        """add node(s) to ring hash"""
        if nodes is None:
            return
        if not isinstance(nodes, list):
            nodes = [nodes]
        self._add_nodes(nodes)

    def __str__(self):
        return f"ring_hash [len={len(self._nodes)}]"

    def __len__(self):
        """size of ring hash"""
        return len(self._nodes)
