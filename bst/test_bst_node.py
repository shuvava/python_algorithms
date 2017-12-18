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

from bst_node import Node
from bst_print import bst_print

class Unit_test_bst_find(unittest.TestCase):
    def setUp(self):
        self.bst_data = [49, 46, 79, 43, 64, 83, 40, 81, 87]
    
    def test_rank(self):
        arr = [item for item in self.bst_data]
        item = arr.pop(0)
        root = Node(item)
        node = root
        while arr:
            item = arr.pop(0)
            parent = node
            node = Node(item)
            parent.left = node
        self.assertEqual(root.rank, 9)
        node.parent.parent.left = None
        self.assertEqual(root.rank, 7)

    def test_level(self):
        arr = [item for item in self.bst_data]
        item = arr.pop(0)
        root = Node(item)
        node = root
        while arr:
            item = arr.pop(0)
            parent = node
            node = Node(item)
            parent.left = node
        self.assertEqual(node.level, 8)
        test_node = node.parent.parent
        test_node.parent = None
        self.assertEqual(test_node.level, 0)
        self.assertEqual(test_node.left.left.level, 2)

if __name__ == '__main__':
    unittest.main()
