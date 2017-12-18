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
import os
from sys import path

from bst_base import BST

__print__ = False
# path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../common')))
# from file_operations import read_array_file, save_array_file

class Unit_test_base_bst(unittest.TestCase):
    def setUp(self):
        self.bst_data = [49, 46, 79, 43, 64, 83, 40, 81, 87]
        #self.bst_data = [49, 46, 79, 43, 64, 83, 40, 81, 87]

    def test_add_node(self):
        bst = BST()
        for node in self.bst_data:
            bst.add_node(node)
        self.assertIsNotNone(bst.root.left)
        self.assertIsNotNone(bst.root.left.left)
        self.assertEqual(bst.root.left.left.value, 43)
        self.assertEqual(bst.length , len(self.bst_data))

    def test_delete_node(self):
        bst = BST().from_list(self.bst_data)
        bst.delete_node(bst.root.left)
        self.assertEqual(bst.length , len(self.bst_data) - 1)

    def test_from_list(self):
        bst = BST().from_list(self.bst_data)
        self.assertIsNotNone(bst.root.left)
        self.assertIsNotNone(bst.root.left.left)
        self.assertEqual(bst.root.left.left.value, 43)

    def test_to_list(self):
        bst = BST().from_list(self.bst_data)
        arr = bst.to_list()
        self.assertIsNotNone(arr)
        self.assertListEqual(sorted(arr), sorted(self.bst_data), 'to list test')

    def test_bst_generation(self):
        bst1 = BST.generate(5)
        bst2 = BST.generate(5)
        self.assertIsNotNone(bst1)
        self.assertIsNotNone(bst1)
        self.assertEqual(bst1.length, 5)
        self.assertNotEqual(bst1.root.value, bst2.root.value)

    def test_bst_print(self):
        bst = BST().from_list(self.bst_data)
        bst.print_tree()
    
    def test_bst_rank(self):
        bst = BST().from_list(self.bst_data)
        self.assertEqual(bst.root.right.rank, 5, 'test_bst_rank')
        self.assertEqual(bst.root.rank, 9)

    def test_is_left_child(self):
        bst = BST().from_list(self.bst_data)
        self.assertTrue(bst.root.left.is_left_child)
        self.assertFalse(bst.root.right.is_left_child)

    def test_is_right_child(self):
        bst = BST().from_list(self.bst_data)
        self.assertTrue(bst.root.right.is_right_child)
        self.assertFalse(bst.root.left.is_right_child)

    def test_is_bst_property_violated(self):
        bst = BST().from_list(self.bst_data)
        self.assertTrue(bst.is_valid)

if __name__ == '__main__':
    __print__ = True
    unittest.main()