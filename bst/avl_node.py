#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
"""
Implements base functionality of AVL node
extends base functionality of BST node

:Properties:
Support all properties of general BST

For every node, require heights of left & right children to differ by at most ±1.
• treat nil tree as height -1
• each node stores its height (DATA STRUCTURE AUGMENTATION) (like subtree
size) (alternatively, can just store difference in heights)

insert each item into AVL tree Θ(n lg n)
"""
from math import fabs

from bst.bst_node import Node


def bst_fix_node_height(node, height):
    """changes height value for parent nodes during tree update"""
    if not node:
        return
    if node._height < height + 1:
        node._height = height + 1
        bst_fix_node_height(node.parent, height + 1)


def bst_fix_node_height_decrease(node, is_left):
    if not node:
        return
    if is_left:
        node._height = node.right_height + 1
    else:
        node._height = node.left_height + 1
    bst_fix_node_height_decrease(node.parent, node.is_left_child)


class AVL_Node(Node):
    def __init__(self, value):
        super().__init__(value)
        self._height = 0

    @property
    def height(self):
        """height of node = length (# edges) of longest downward path to a leaf"""
        return self._height

    @property
    def left_height(self):
        """return height left sub tree"""
        if not self.left:
            return -1
        return self.left.height

    @property
    def right_height(self):
        """return height right sub tree"""
        if not self.right:
            return -1
        return self.right.height

    def set_parent(self, node):
        """set link to parent node"""
        if node and not isinstance(node, Node):
            return False
        if not node and self.parent:
            # fix decreasing height
            bst_fix_node_height_decrease(self.parent, self.is_left_child)
        super().set_parent(node)
        if node:
            bst_fix_node_height(self.parent, self._height)
        return True

    def get_is_valid(self):
        """check violation of AVL node properties"""
        if not super().get_is_valid():
            return False
        if fabs(self.left_height - self.right_height) < 2:
            return True
        return False

