#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2017-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
class implements base functionality of node of BST

:Properties:

Each node x in the binary tree has a key key(x).
Nodes other than the root have a parent p(x).
Nodes may have a left child lef t(x) and/or a right child right(x).
These are pointers unlike in a heap.
The invariant is: for any node x,
for all nodes y in the left subtree of x, key(y) ≤ key(x).
For all nodes y in the right subtree of x key(y) ≥ key(x).
"""


def bst_fix_node_rank(node, removed_items):
    """changes rank value for parents nodes during tree update"""
    while node:
        node._rank += removed_items
        node = node.parent


def bst_fix_node_level(node, level):
    """changes level value for children nodes during tree update"""
    if not node:
        return
    node._level = level + 1
    bst_fix_node_level(node.left, node._level)
    bst_fix_node_level(node.right, node._level)


class Node:
    """base functionality of BST"""

    def __init__(self, value):
        self._value = value
        self._parent = None
        self._left = None
        self._right = None
        self._level = 0
        self._rank = 1

    @property
    def parent(self):
        """get link to parent node"""
        return self._parent

    def set_parent(self, node):
        """set link to parent node"""
        if node and not isinstance(node, Node):
            return False
        self._parent = node
        if node:
            bst_fix_node_level(self, node.level)
        else:
            bst_fix_node_level(self, -1)
        return True

    @parent.setter
    def parent(self, node):
        self.set_parent(node)

    @property
    def value(self):
        """node value"""
        return self._value

    @property
    def rank(self):
        """count of nodes subtree include current"""
        return self._rank

    @property
    def level(self):
        """count of parents nodes to root 0 if root"""
        return self._level

    @property
    def left(self):
        """get left child"""
        return self._left

    @left.setter
    def left(self, node):
        """set left child"""
        if node and not isinstance(node, Node):
            return
        if self._left:
            bst_fix_node_rank(self, -self._left.rank)
        if node:
            node.parent = self
            bst_fix_node_rank(self, node.rank)
        self._left = node

    @property
    def right(self):
        """get right child"""
        return self._right

    @right.setter
    def right(self, node):
        """set right child"""
        if node and not isinstance(node, Node):
            return
        if self._right:
            bst_fix_node_rank(self, -self._right.rank)
        if node:
            node.parent = self
            bst_fix_node_rank(self, node.rank)
        self._right = node

    @property
    def is_left_child(self):
        """True if this node is left child of parent"""
        if not self.parent:
            return False
        if self.parent.left is self:
            return True
        return False

    @property
    def is_right_child(self):
        """True if this node is right child of parent"""
        if not self.parent:
            return False
        if self.parent.right is self:
            return True
        return False

    @property
    def children_count(self):
        """count of children of current elemnet"""
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def get_is_valid(self):
        """check violation of BST node properties"""
        if self.left and self.left.value >= self.value:
            return False
        if self.right and self.right.value < self.value:
            return False
        return True

    @property
    def is_valid(self):
        return self.get_is_valid()
