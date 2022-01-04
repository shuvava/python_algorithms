#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2019-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Disjoint-set data structure
implements union-by-rank, path compression, and size queries
"""


class DisjointSet:
    """Represents a set of disjoint sets. Also known as the union-find data structure.
    Main operations are querying if two elements are in the same set, and merging two sets together.
    Useful for testing graph connectivity, and is used in Kruskal's algorithm.
    """

    def __init__(self, numelems):
        """Constructs a new set containing the given number of singleton sets.
        For example, DisjointSet(3) --> {{0}, {1}, {2}}.
        """
        if numelems < 0:
            raise ValueError('Number of elements must be non-negative')

        # A global property
        self.num_sets = numelems

        # Per-node properties (three):
        # The index of the parent element. An element is a representative iff its parent is itself.
        self.parents = list(range(numelems))
        # Always in the range [0, floor(log2(numelems))].
        self.ranks = [0] * numelems
        # Positive number if the element is a representative, otherwise zero.
        self.sizes = [1] * numelems

    def get_num_elements(self):
        """Returns the number of elements among the set of disjoint sets; this was the number passed
        into the constructor and is constant for the lifetime of the object. All the other methods
        require the argument elemindex to satisfy 0 <= elemindex < get_num_elements().
        """
        return len(self.parents)

    def get_num_sets(self):
        """Returns the number of disjoint sets overall. This number decreases monotonically as time progresses;
        each call to merge_sets() either decrements the number by one or leaves it unchanged.
         0 <= result <= get_num_elements().
        """
        return self.num_sets

    def _get_repr(self, elemindex):
        """(Private) Returns the representative element for the set containing the given element. This method is also
        known as 'find' in the literature. Also performs path compression, which alters the internal state to
        improve the speed of future queries, but has no externally visible effect on the values returned.
        """
        if not (0 <= elemindex < len(self.parents)):
            raise IndexError()
        # Follow parent pointers until we reach a representative
        parent = self.parents[elemindex]
        if parent == elemindex:
            return elemindex
        while True:
            grandparent = self.parents[parent]
            if grandparent == parent:
                return parent
            # Partial path compression
            self.parents[elemindex] = grandparent
            elemindex = parent
            parent = grandparent

    def get_size_of_set(self, elemindex):
        """Returns the size of the set that the given element is a member of. 1 <= result <= get_num_elements().
        """
        return self.sizes[self._get_repr(elemindex)]

    def are_in_same_set(self, elemindex0, elemindex1):
        """Tests whether the given two elements are members of the same set. Note that the arguments are orderless.
        """
        return self._get_repr(elemindex0) == self._get_repr(elemindex1)

    def merge_sets(self, elemindex0, elemindex1):
        """Merges together the sets that the given two elements belong to.
        This method is also known as 'union' in the literature.
        If the two elements belong to different sets, then the two sets are merged and the method returns True.
        Otherwise they belong in the same set, nothing is changed and the method returns False.
        Note that the arguments are orderless.
        """
        # Get representatives
        repr0 = self._get_repr(elemindex0)
        repr1 = self._get_repr(elemindex1)
        if repr0 == repr1:
            return False

        # Compare ranks
        cmp = self.ranks[repr0] - self.ranks[repr1]
        if cmp == 0:  # Increment repr0's rank if both nodes have same rank
            self.ranks[repr0] += 1
        elif cmp < 0:  # Swap to ensure that repr0's rank >= repr1's rank
            repr0, repr1 = repr1, repr0

        # Graft repr1's subtree onto node repr0
        self.parents[repr1] = repr0
        self.sizes[repr0] += self.sizes[repr1]
        self.sizes[repr1] = 0
        self.num_sets -= 1
        return True
