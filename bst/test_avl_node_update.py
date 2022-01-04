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

from avl_node import AVL_Node
from avl_node_update import rotation_left, rotation_right, rotation, avl_insert, avl_delete
from bst_print import bst_print

__print_trees__ = False


def create_left_heavy_tree(avl_data):
    arr = [item for item in avl_data]
    item = arr.pop(0)
    root = AVL_Node(item)
    node = root
    while arr:
        item = arr.pop(0)
        parent = node
        node = AVL_Node(item)
        parent.left = node
    return (root, node)


def create_right_heavy_tree(avl_data):
    arr = [item for item in avl_data]
    item = arr.pop(0)
    root = AVL_Node(item)
    node = root
    while arr:
        item = arr.pop(0)
        parent = node
        node = AVL_Node(item)
        parent.right = node
    return (root, node)


class Unit_test_avl_node_update(unittest.TestCase):
    def setUp(self):
        self.bst_data = [40, 43, 46, 49, 64, 79, 81, 83, 87]

    def test_rotation_left_border_cases(self):
        result = rotation_left(1)
        self.assertIsNone(result, 'only AVL_Node object allowed to rotate')
        result = rotation_left(AVL_Node(1))
        self.assertIsNone(result, 'element should have at least one left child')

    def test_rotation_right_border_cases(self):
        result = rotation_right(1)
        self.assertIsNone(result, 'only AVL_Node object allowed to rotate')
        result = rotation_right(AVL_Node(1))
        self.assertIsNone(result, 'element should have at least one left child')

    def test_rotation_left(self):
        if __print_trees__:
            print('test_rotation_left>>>>')
        tree = create_left_heavy_tree([51, 49, 46, 43])
        root = tree[0]
        elm = root.left
        last = tree[1]
        if __print_trees__:
            bst_print(root)
        self.assertEqual(root.height, 3, 'test dataset height is 3')
        self.assertFalse(elm.is_valid, 'ivalid AVL property')
        new_elm = rotation_left(elm)
        if __print_trees__:
            bst_print(root)
        self.assertEqual(root.height, 2, 'corrected tree height should be 2')
        self.assertEqual(new_elm.height, 1, 'rotated element height should be 1')
        self.assertTrue(new_elm.is_valid, 'ivalid AVL property')
        if __print_trees__:
            print('<<<<test_rotation_left')

    def test_rotation_right(self):
        if __print_trees__:
            print('test_rotation_right>>>>')
        tree = create_right_heavy_tree([51, 43, 46, 49])
        root = tree[0]
        elm = root.right
        last = tree[1]
        if __print_trees__:
            bst_print(root)
        self.assertEqual(root.height, 3, 'test dataset height is 3')
        self.assertFalse(elm.is_valid, 'ivalid AVL property')
        new_elm = rotation_right(elm)
        if __print_trees__:
            bst_print(root)
        self.assertEqual(root.height, 2, 'corrected tree height should be 2')
        self.assertEqual(new_elm.height, 1, 'rotated element height should be 1')
        self.assertTrue(new_elm.is_valid, 'ivalid AVL property')
        if __print_trees__:
            print('<<<<test_rotation_right')

    def test_rotation_left_with_children(self):
        if __print_trees__:
            print('test_rotation_left_with_children>>>>')
        root = AVL_Node(51)
        elm = AVL_Node(49)
        root.left = elm
        elm.left = AVL_Node(46)
        elm.left.right = AVL_Node(47)
        elm.left.left = AVL_Node(43)
        if __print_trees__:
            bst_print(root)
        self.assertEqual(root.height, 3, 'test dataset height is 3')
        self.assertFalse(elm.is_valid, 'ivalid AVL property')
        new_root = rotation_left(elm)
        if __print_trees__:
            bst_print(root)
        self.assertEqual(root.height, 3, 'corrected tree height should be 3')
        self.assertTrue(new_root.is_valid, 'ivalid AVL property')
        if __print_trees__:
            print('<<<<test_rotation_left_with_children')

    def test_rotation_right_with_children(self):
        if __print_trees__:
            print('test_rotation_right_with_children>>>>')
        root = AVL_Node(51)
        elm = AVL_Node(43)
        root.left = elm
        elm.right = AVL_Node(46)
        elm.right.right = AVL_Node(49)
        elm.right.left = AVL_Node(44)
        if __print_trees__:
            bst_print(root)
        self.assertEqual(root.height, 3, 'test dataset height is 3')
        self.assertFalse(elm.is_valid, 'ivalid AVL property')
        new_root = rotation_right(elm)
        if __print_trees__:
            bst_print(root)
        self.assertEqual(root.height, 3, 'corrected tree height should be 3')
        self.assertTrue(new_root.is_valid, 'ivalid AVL property')
        if __print_trees__:
            print('<<<<test_rotation_right_with_children')

    def test_rotation(self):
        root = AVL_Node(43)
        result = rotation(root)
        self.assertIsNone(result)
        root.left = AVL_Node(46)
        result = rotation(root)
        self.assertIsNotNone(result)
        root = result
        root.left = AVL_Node(44)
        result = rotation(root)
        self.assertIsNone(result)

    def test_avl_insert(self):
        if __print_trees__:
            print('test_avl_insert >>>>')
        arr = [item for item in self.bst_data]
        item = arr.pop(0)
        root = AVL_Node(item)
        while arr:
            item = arr.pop(0)
            node = AVL_Node(item)
            root = avl_insert(root, node)
        if __print_trees__:
            bst_print(root)
        self.assertEqual(root.value, 49)
        self.assertEqual(root.height, 3)
        self.assertTrue(root.is_valid)
        if __print_trees__:
            print('<<<< test_avl_insert')

    def test_avl_delete(self):
        if __print_trees__:
            print('test_avl_delete >>>>')
        root = AVL_Node(43)
        root.left = AVL_Node(32)
        root.right = AVL_Node(46)
        root.left.left = AVL_Node(30)
        root.left.right = AVL_Node(36)
        if __print_trees__:
            bst_print(root)
        self.assertTrue(root.is_valid)
        new_root = avl_delete(root.right)
        if __print_trees__:
            bst_print(new_root)
        self.assertTrue(new_root.is_valid)
        if __print_trees__:
            print('<<<< test_avl_delete')


if __name__ == '__main__':
    __print_trees__ = True
    unittest.main()
