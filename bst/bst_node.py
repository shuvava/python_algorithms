#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
class implements base functionality of node of BST

:Properties:

Each node x in the binary tree has a key key(x).
Nodes other than the root have a parent p(x).
Nodes may have a left child lef t(x) and/or a right child right(x).
These are pointers unlike in a heap.
The invariant is: for any node x,
for all nodes y in the left subtree of x, key(y) ≤ key(x).
For all nodes y in the right subtree of x key(y) ≥ key(x).
'''
class Node:
    def __init__(self, value, parent=None):
        self._value = value
        self._parent = None
        self._left = None
        self._right = None
        self._level = 0
        self._rank = 1
        # set object properties
        if parent:
            self._parent = parent
            self._level = parent.level + 1

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        if value and isinstance(value, Node):
            self._parent = value

    @property
    def value(self):
        return self._value

    @property
    def rank(self):
        return self._rank

    @property
    def level(self):
        return self._level;

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        if node and not isinstance(node, Node):
            return
        self._left = node
        if node:
            node.parent = self
            node._level = self._level + 1


    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        if node and not isinstance(node, Node):
            return
        self._right = node
        if node:
            node.parent = self
            node._level = self._level + 1

    @property
    def is_left_child(self):
        if not self.parent:
            return False
        if self.parent.left is self:
            return True
        return False

    @property
    def is_right_child(self):
        if not self.parent:
            return False
        if self.parent.right is self:
            return True
        return False

    @property
    def children_count(self):
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt


