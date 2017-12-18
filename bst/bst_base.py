#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
implement base functionality of parsing dict into tree structure

:Properties:

Each node x in the binary tree has a key key(x).
Nodes other than the root have a parent p(x).
Nodes may have a left child lef t(x) and/or a right child right(x).
These are pointers unlike in a heap.
The invariant is: for any node x,
for all nodes y in the left subtree of x, key(y) <= key(x).
For all nodes y in the right subtree of x key(y) >= key(x).

balanced BST maintains h = O(lg n) ⇒ all operations run in O(lg n) time
'''
import random
from bst_node import Node
from bst_node_query import bst_to_list, bst_search, bst_is_properties_valid
from bst_node_update import bst_insert, bst_delete
from bst_print import bst_print

def gen_array(length, max_value=1000):
    '''Generates random array
    Parameters
    ----------
    length: int
        the length of random array
    Returns
    -------
        list of random elements
    '''
    _data = []
    _i = 0
    while _i < length:
        _data.append(random.randrange(1, max_value))
        _i += 1
    return _data


class BST(object):
    '''Binary search tree base functionality
    '''
    def __init__(self):
        self._root = None
        self._length = 0

    @property
    def root(self):
        return self._root

    @property
    def length(self):
        return self._length

    @root.setter
    def root(self, value):
        '''get root of tree'''
        if value and isinstance(value, Node):
            self._root = value

    def add_node(self, node):
        '''Adding node into BST'''
        if not isinstance(node, Node):
            node = Node(node)
        self._length += 1
        if self.root == None:
            self.root = node
            return
        return bst_insert(self.root, node)

    def delete_node(self, node):
        '''Remove a node from BST'''
        _node = node
        if not isinstance(node, Node):
             _node = bst_search(self.root, node)
        if _node is self.root:
            raise NotImplementedError
        bst_delete(_node)
        self._length -= 1

    def to_list(self):
        '''Converts current BST object into dict object'''
        if not self.root:
            return []
        return bst_to_list(self.root, [])

    @property
    def is_valid(self):
        return bst_is_properties_valid(self.root)

    def from_list(self, arr):
        '''Converts dict object into BST class instance
        
        :Parameters:
        arr: *list* - array of int for generating BST tree
        '''
        if not isinstance(arr, list):
            return
        #bst = BST()
        for item in arr:
            self.add_node(item)
        return self

    @staticmethod
    def generate(size, max_value=1000):
        '''generate random BST
        
        :Parameters:
        size: *int* - length of BST
        max_value: *int* max element value
        '''
        arr = gen_array(size, max_value)
        return BST().from_list(arr)

    def print_tree(self, node = None, with_values=True):
        '''print BST
        
        :Parameters:
        node: *Node* - start node of printing tree (*default root node*)
        with_values: *Boolean* - print value of element in array(*default True*)
        '''
        if not node:
            node = self.root
        bst_print(node, with_values)