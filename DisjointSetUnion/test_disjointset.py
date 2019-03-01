#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
Test of base_bst module
https://docs.python.org/3/library/unittest.html
'''
import unittest
from disjointset import DisjointSet

class UnitTestDisjointSet(unittest.TestCase):
    def test_add_item(self):
        #arrange
        dt = DisjointSet()
        #act
        dt.add(1)
        dt.add(2)
        dt.add(3)
        #assert
        self.assertEqual(sum(dt.sizes.values()), 3)
        self.assertEqual(dt.parents[3], 3)

    def test_union(self):
        #arrange
        dt = DisjointSet()
        dt.add(1)
        dt.add(2)
        dt.add(3)
        dt.add(4)
        dt.add(5)
        #act
        dt.union(1, 4)

        dt.union(3, 5)
        dt.union(5, 2)
        #assert
        self.assertEqual(dt.parents[4], 1)
        self.assertEqual(dt.parents[1], 1)
        self.assertEqual(dt.sizes[1], 2)
        self.assertTrue(4 not in dt.sizes)

        self.assertEqual(dt.parents[3], 3)
        self.assertEqual(dt.parents[5], 3)
        self.assertEqual(dt.parents[2], 3)
        self.assertEqual(dt.sizes[3], 3)
        self.assertTrue(5 not in dt.sizes)
        self.assertTrue(2 not in dt.sizes)

if __name__ == '__main__':
    unittest.main()
