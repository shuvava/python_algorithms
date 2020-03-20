#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
#
"""
Disjoint-set data structure
implements path compression
original https://github.com/alexgolec/interview-problems/blob/master/synonymous-queries/transitivity_disjoint_set.py
"""


class DisjointSet:
    def __init__(self):
        self.parents = {}
        self.sizes = {}

    def add(self, item):
        if item not in self.parents:
            self.parents[item] = item
            self.sizes[item] = 1

    def get_root(self, item):
        visited = []
        while self.parents[item] != item:
            visited.append(item)
            item = self.parents[item]
        # compress path
        for node in visited:
            self.parents[node] = item
        return item

    def union(self, item1, item2):
        if item1 not in self.parents:
            return False
        if item2 not in self.parents:
            return False
        root1 = self.get_root(item1)
        root2 = self.get_root(item2)
        if root1 == root2:
            return False

        # Compare sizes
        if self.sizes[root1] - self.sizes[root2] < 0:
            root1, root2 = root2, root1
        self.parents[root2] = root1
        self.sizes[root1] += self.sizes[root2]
        del self.sizes[root2]
