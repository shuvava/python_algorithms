#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
Implementation of a priority queue (BST) - HEAP
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec04.pdf
An array, visualized as a nearly complete binary tree 
Definition:
    root of tree: first element in the array, corresponding to i = 1 (0 index of array)
    parent(i) =i/2: returns index of node's parent
    left(i)=2i: returns index of node's left child
    right(i)=2i+1: returns index of node's right child

Max Heap Property: The key of a node is >= than the keys of its children
(Min Heap defined analogously)
'''
from base_bst import BaseBst

class Heap(BaseBst):
    '''Implementation of base functionality of bst- heap
    '''
    def swap(self, i, j):
        '''this method was intensionally made separate to evaluate count of calls'''
        self._array[i], self._array[j] = self._array[j], self._array[i]

    def get_root(self):
        '''return root of heap (first element in the array)
        '''
        return 0

    def left(self, index):
        '''left(i)=2(i+1): returns index of node's left child

        :param index: index of element
        :type index: Number
        '''
        if index < self.get_root():
            return self.get_root()
        left = 2*(index) + 1
        if left < len(self._array):
            return left
        return None

    def right(self, index):
        '''right(i)=2i: returns index of node's right child

        :param index: index of element
        :type index: Number
        '''
        if index < self.get_root():
            return self.get_root()
        right = 2*(index + 1)
        if right < len(self._array):
            return right
        return None

    def max_heapify(self, index=None):
        '''correct a single violation of the heap property in a subtree at its root
        :Heap Property: *The key of a node is >= than the keys of its children*
        
        :param index: index of element (*default None == Root element of heap*)
        :type index: Number
        '''
        if not self._array:# empty array
            return
        if  index is None or index < self.get_root():# fix the first element
            index = self.get_root()
        #init variables
        left = self.left(index)
        right = self.right(index)
        largest = index

        if left is not None and self._array[left] > self._array[index]:
            largest = left
        if right is not None and self._array[right] > self._array[largest]:
            largest = right
        if largest != index:# fix heap and do recursive call
            self.swap(index, largest)
            self.max_heapify(largest)

    def build_max_heap(self):
        '''Converts A[1…n] to a max heap
        Why start at n/2? Because elements A[n/2 + 1 … n] are 
        all leaves of the tree 2i > n, for i > n/2 + 1
        Observe however that Max_Heapify takes O(1) for
        time for nodes that are one level above the leaves, and
        in general, O(l) for the nodes that are l levels above the
        leaves. We have n/4 nodes with level 1, n/8 with level 2,
        and so on till we have one root node that is lg n levels
        above the leaves. 
        '''
        for index in range(int(len(self._array)/2), -1, -1):
            if self.verbosity:
                print('-----------index={}'.format(index))
                self.print_tree(index)
            self.max_heapify(index)
            if self.verbosity:
                self.print_tree(index)

    def main(self, _array):
        '''main entry point'''
        self.set(_array)
        if self.verbosity:
            self.print_tree()
        self.build_max_heap()
        if self.verbosity:
            print('------------------------------------------')
            print(_array)
            self.print_tree()

if __name__ == '__main__':
    Heap().run()
