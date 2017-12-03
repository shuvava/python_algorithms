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

from bst_base import BST
from bst_node import Node
from bst_node_update import bst_insert, bst_delete
from bst_print import bst_print

class Unit_test_bst_node_update(unittest.TestCase):
    def setUp(self):
        self.bst_data = [49, 46, 79, 43, 64, 83, 40, 81, 87]

    def test_bst_insert(self):
        arr = [item for item in self.bst_data]
        item = arr.pop(0)
        root = Node(item)
        while arr:
            item = arr.pop(0)
            node = Node(item)
            bst_insert(root, node)
        self.assertIsNotNone(root.left)
        self.assertIsNotNone(root.left.left)
        self.assertEqual(root.left.left.value, 43)

    def test_bst_delete(self):
        print('--------------------test_bst_delete')
        bst = BST.from_list(self.bst_data)
        bst_delete(bst.root.left.left)
        bst_print(bst.root)
        self.assertEqual(bst.root.left.rank, 2)
        self.assertIsNotNone(bst.root.left.left)
        self.assertIsNone(bst.root.left.left.left)
        bst_delete(bst.root.right)
        self.assertEqual(bst.root.rank, 7)
        bst_print(bst.root)
        print('--------------------test_bst_delete')

if __name__ == '__main__':
    unittest.main()