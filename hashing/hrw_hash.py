#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
#
"""
Rendezvous or highest random weight (HRW) hashing

Properties
    It might first appear sufficient to treat the n sites as buckets in a hash table and hash the object name O into
    this table. However, if any of the sites fails or is unreachable, the hash table size changes, requiring all
    objects to be remapped. This massive disruption makes such direct hashing unworkable. Under rendezvous hashing,
    however, clients handle site failures by picking the site that yields the next largest weight.
    Remapping is required only for objects currently mapped to the failed site, and disruption is minimal.

    Low overhead: The hash function used is efficient, so overhead at the clients is very low.
    Load balancing: Since the hash function is randomizing, each of the n sites is equally likely to receive
    the object O. Loads are uniform across the sites.
    Site capacity: Sites with different capacities can be represented in the site list with multiplicity in proportion
     to capacity. A site with twice the capacity of the other sites will be represented twice in the list,
     while every other site is represented once.
    High hit rate: Since all clients agree on placing an object O into the same site SO , each fetch or placement of
    O into SO yields the maximum utility in terms of hit rate. The object O will always be found unless it is evicted
    by some replacement algorithm at SO.
    Minimal disruption: When a site fails, only the objects mapped to that site need to be remapped.
    Disruption is at the minimal possible level, as proved in.[1][2]
    Distributed k-agreement: Clients can reach distributed agreement
    on k sites simply by selecting the top k sites in the ordering
Drawback
    The biggest drawback of rendezvous hashing is that it runs in O(n) instead of O(log(n)).
    However, because you don’t typically have to break each node into multiple virtual nodes,
    n is typically not large enough for the run-time to be a significant factor.
Links:
    https://en.wikipedia.org/wiki/Rendezvous_hashing
    https://medium.com/i0exception/rendezvous-hashing-8c00e2fb58b0
"""
import math
from typing import List

from murmur3 import murmur3_hash


def int_to_float(value: int) -> float:
    """Converts a uniformly random [[64-bit computing|64-bit]] integer
    to uniformly random floating point number on interval <math>[0, 1)</math>."""
    fifty_three_ones = 0xFFFFFFFFFFFFFFFF >> (64 - 53)
    fifty_three_zeros = float(1 << 53)
    return (value & fifty_three_ones) / fifty_three_zeros


class Node:
    """Class representing a node that is assigned keys as part of a weighted rendezvous hash."""

    def __init__(self, name: str, seed: int, weight: int) -> None:
        self.name, self.seed, self.weight = name, seed, weight

    def __str__(self):
        return f"[{self.name} ({str(self.seed)}, {str(self.weight)})]"

    def compute_weighted_score(self, key):
        hash_2 = murmur3_hash(str(key), 0xFFFFFFFF & self.seed)
        hash_f = int_to_float(hash_2)
        score = 1.0 / -math.log(hash_f)
        return self.weight * score


def determine_responsible_node(nodes: List[Node], key: str) -> Node:
    """Determines which node, of a set of nodes of various weights, is responsible for the provided key.
    Examples:
        >>> import hashing.hrw_hash as wrh
        >>> node1 = wrh.Node("node1", 123, 100)
        >>> node2 = wrh.Node("node2", 567, 200)
        >>> node3 = wrh.Node("node3", 789, 300)
        >>> str(wrh.determine_responsible_node([node1, node2, node3], 'foo'))
        '[node3 (789, 300)]'
        >>> str(wrh.determine_responsible_node([node1, node2, node3], 'bar'))
        '[node3 (789, 300)]'
        >>> str(wrh.determine_responsible_node([node1, node2, node3], 'hello'))
        '[node2 (567, 200)]'
    """
    highest_score, champion = -1, None
    for node in nodes:
        score = node.compute_weighted_score(key)
        if score > highest_score:
            champion, highest_score = node, score
    return champion
