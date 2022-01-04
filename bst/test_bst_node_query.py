#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2017-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
Test of base_bst module
https://docs.python.org/3/library/unittest.html
'''
import unittest

from bst.bst_base import BST
from bst.bst_node_query import bst_find_smaller, bst_count, \
    bst_max, bst_min, bst_search, bst_next_larger, bst_next_smaller
from bst.bst_print import bst_print

__print_trees__ = False


class Unit_test_bst_find(unittest.TestCase):
    def setUp(self):
        self.bst_data = [49, 46, 79, 43, 64, 83, 40, 81, 87]
        bst = BST().from_list(self.bst_data)
        if __print_trees__:
            bst_print(bst.root)

    def test_bst_find_smaller(self):
        bst = BST().from_list(self.bst_data)
        node = bst_find_smaller(bst.root, 45)
        self.assertEqual(node.value, 43)

    def test_count_of_less_or_equal(self):
        bst = BST().from_list(self.bst_data)
        count = bst_count(bst.root, 45)
        self.assertEqual(count, 2)
        count = bst_count(bst.root, 79)
        self.assertEqual(count, 6)

    def test_max(self):
        bst = BST().from_list(self.bst_data)
        max_value = bst_max(bst.root)
        self.assertEqual(max_value, max(self.bst_data))

    def test_min(self):
        bst = BST().from_list(self.bst_data)
        min_value = bst_min(bst.root)
        self.assertEqual(min_value, min(self.bst_data))

    def test_search(self):
        bst = BST().from_list(self.bst_data)
        # test is found result
        result = bst_search(bst.root, 64)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 64)
        # test is not found result
        result = bst_search(bst.root, 66)
        self.assertIsNone(result)

    def test_next_larger(self):
        bst = BST().from_list(self.bst_data)
        # test go right by tree
        result = bst_next_larger(bst.root, 65)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 79)
        # test go right by  tree
        result = bst_next_larger(bst.root, 44)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 46)
        # test go left right by tree
        result = bst_next_larger(bst.root, 63)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 64, 'test go left right by tree')
        result = bst_next_larger(bst.root, 82)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 83, 'test go left right by tree')

    def test_next_smaller(self):
        if __print_trees__:
            print('test_next_smaller >>>>')
        bst = BST().from_list(self.bst_data)
        # test go right by tree
        result = bst_next_smaller(bst.root, 65)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 64)
        # test go right by  tree
        result = bst_next_smaller(bst.root, 44)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 43)
        # test go left right by tree
        result = bst_next_smaller(bst.root, 63)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 49, 'test go left right by tree')
        result = bst_next_smaller(bst.root, 82)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 81, 'test go left right by tree')
        if __print_trees__:
            print('<<<< test_next_smaller')

    def test_to_list(self):
        bst = BST().from_list(self.bst_data)
        arr = []
        arr = bst.to_list()
        self.assertIsNotNone(arr)
        self.assertListEqual(sorted(arr), sorted(self.bst_data), 'to list test')


if __name__ == '__main__':
    __print_trees__ = True
    unittest.main()
