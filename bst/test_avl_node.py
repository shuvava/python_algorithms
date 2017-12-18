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

from avl_node import AVL_Node

class Unit_test_bst_find(unittest.TestCase):
    def setUp(self):
        self.bst_data = [49, 46, 79, 43, 64, 83, 40, 81, 87]

    def test_height(self):
        arr = [item for item in self.bst_data]
        item = arr.pop(0)
        root = AVL_Node(item)
        node = root
        while arr:
            item = arr.pop(0)
            parent = node
            node = AVL_Node(item)
            parent.left = node

        self.assertEqual(node.height, 0, 'low level always 0')
        self.assertEqual(root.right_height, -1, 'None child should have -1 height')
        self.assertEqual(root.height, len(self.bst_data)-1, 'root equal height of tree')

        test_node = node.parent.parent
        test_node.parent = None
        self.assertEqual(test_node.height, 2, 'root height after tree update')
        self.assertEqual(test_node.left.left.height, 0,'low level height after tree update')

    def test_avl_property(self):
        arr = [item for item in self.bst_data]
        item = arr.pop(0)
        root = AVL_Node(item)
        node = root
        while arr:
            item = arr.pop(0)
            parent = node
            node = AVL_Node(item)
            parent.left = node

        self.assertFalse(root.is_valid)

if __name__ == '__main__':
    unittest.main()
