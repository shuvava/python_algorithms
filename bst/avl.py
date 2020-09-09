#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
"""
An AVL tree is another balanced binary search tree.
Named after their inventors,
Adelson-Velskii and Landis, they were the first dynamically
balanced trees to be proposed

balanced BST maintains h = O(lg n) ⇒ all operations run in O(lg n) time

:Properties:
Support all properties of general BST

For every node, require heights of left & right children to differ by at most ±1.
• treat nil tree as height -1
• each node stores its height (DATA STRUCTURE AUGMENTATION) (like subtree
size) (alternatively, can just store difference in heights)
"""
from bst.avl_node import AVL_Node
from bst.avl_node_update import avl_insert, avl_delete
from bst.bst_base import BST
from bst.bst_node_query import bst_search


class AVL(BST):
    """Implements core functionality of AVl tree"""

    def __init__(self):
        super().__init__()

    def add_node(self, node):
        """Adding node into BST"""
        if not isinstance(node, AVL_Node):
            node = AVL_Node(node)
        self._length += 1
        if self.root is None:
            self.root = node
            return
        self.root = avl_insert(self.root, node)

    def delete_node(self, node):
        """Remove a node from BST"""
        _node = node
        if not isinstance(node, AVL_Node):
            _node = bst_search(self.root, node)
        if _node is self.root:
            raise NotImplementedError
        self.root = avl_delete(_node)
        self._length -= 1
