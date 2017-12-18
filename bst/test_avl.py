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

from avl import AVL
from bst_print import bst_print

__print__ = False

class Unit_test_AVL(unittest.TestCase):
    def setUp(self):
        self.bst_data = [40, 43, 46, 49, 64, 79, 81, 83, 87]

    def test_add_node(self):
        bst = AVL()
        for node in self.bst_data:
            bst.add_node(node)
        self.assertEqual(bst.length , len(self.bst_data))
        self.assertEqual(bst.root.value, 49)

    def test_delete_node(self):
        if __print__:
            print('test_delete_node >>>>')
        bst = AVL().from_list(self.bst_data)
        if __print__:
            bst.print_tree()
        bst.delete_node(bst.root.left)
        if __print__:
            bst.print_tree()
        self.assertEqual(bst.length , len(self.bst_data) - 1)
        if __print__:
            print('<<<< test_delete_node')

if __name__ == '__main__':
    __print__ = True
    unittest.main()
