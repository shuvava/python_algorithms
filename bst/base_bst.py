#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
Implementation of binary search tree (BST) - HEAP
Definition:
    root of tree: first element in the array, corresponding to i = 1 (0 index of array)
    parent(i) =i/2: returns index of node's parent
    left(i)=2i: returns index of node's left child
    right(i)=2i+1: returns index of node's right child
'''
import abc
from base_interface import BaseAlg

class BaseBst(BaseAlg, metaclass=abc.ABCMeta):
    '''Implementation of base functionality of bst- heap
    '''
    def __init__(self, array_=None):
        super().__init__()
        if array_ is not None and isinstance(array_, list):
            self._array = array_
        else:
            self._array = []

    def set(self, array_):
        '''initialize array as a heap

        :param array_: array of elements
        :type array_: list
        '''
        if array_ is None or not isinstance(array_, list):
            return
        self._array = array_

    @abc.abstractmethod
    def get_root(self):
        '''Get root element of tree'''
        raise NotImplementedError('algorithm should be implemented')

    @abc.abstractmethod
    def left(self, index):
        '''Get right child of element'''
        raise NotImplementedError('algorithm should be implemented')

    @abc.abstractmethod
    def right(self, index):
        '''Get right child of element'''
        raise NotImplementedError('algorithm should be implemented')

    def _print_tree(self, index, with_ids=False, with_values=True):
        '''Recursive function used for pretty-printing the binary tree.
        In each recursive call, a "box" of characters visually representing the
        current subtree is constructed line by line. Each line is padded with
        whitespaces to ensure all lines have the same length. The box, its width,
        and the start-end positions of its root (used for drawing branches) are
        sent up to the parent call, which then combines left and right sub-boxes
        to build a bigger box etc.'''
        if not self._array or index is None or index < self.get_root():
            return [], 0, 0, 0
        if with_ids and with_values:
            node_repr = '{}:{}'.format(index, self._array[index])
        elif with_ids and not with_values:
            node_repr = str(index)
        elif not with_ids and with_values:
            node_repr = str(self._array[index])
        else:  # pragma: no cover
            node_repr = 'O'
        line1 = []
        line2 = []
        new_root_width = gap_size = len(node_repr)

        # Get the left and right sub-boxes, their widths and their root positions
        l_box, l_box_width, l_root_start, l_root_end = \
            self._print_tree(self.left(index), with_ids, with_values)
        r_box, r_box_width, r_root_start, r_root_end = \
            self._print_tree(self.right(index), with_ids, with_values)

        # Draw the branch connecting the new root to the left sub-box,
        # padding with whitespaces where necessary
        if l_box_width > 0:
            l_root = -int(-(l_root_start + l_root_end) / 2) + 1  # ceiling
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        # Draw the representation of the new root
        line1.append(node_repr)
        line2.append(' ' * new_root_width)

        # Draw the branch connecting the new root to the right sub-box,
        # padding with whitespaces where necessary
        if r_box_width > 0:
            r_root = int((r_root_start + r_root_end) / 2)  # floor
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root + 1))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        # Combine the left and right sub-boxes with the branches drawn above
        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)

        # Return the new box, its width and its root positions
        return new_box, len(new_box[0]), new_root_start, new_root_end

    def print_tree(self, index=0, with_ids=False, with_values=True):
        '''print BTS tree starting from index
        
        :Parameters:
        index: *Number* - start index of printing tree
        with_ids: *Boolean* - print index of element in array (*default False*)
        with_values: *Boolean* - print value of element in array(*default True*)
        '''
        tree_str_ = '\n' + '\n'.join(self._print_tree(index, with_ids, with_values)[0])
        print(tree_str_)

    @abc.abstractmethod
    def main(self, _array):
        '''Algorithm implementation '''
        raise NotImplementedError('algorithm should be implemented')
