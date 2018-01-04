#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
Implementation Heap sort
Running time:
after n iterations the Heap is empty
every iteration involves a swap and a max_heapify
operation; hence it takes O(log n) time

Complexity: O(n*ln(n))
'''
#add parent directory with base module
from sys import path
path.insert(0, '../bst')

from heap import Heap

class HeapSort(Heap):
    '''Implementation of Heap sort
    '''
    def heap_sort(self):
        '''Sorting Strategy:
        1. Build Max Heap from unordered array;
        2. Find maximum element A[1];
        3. Swap elements A[n] and A[1]:
        now max element is at the end of the array!
        4. Discard node n from heap
        (by decrementing heap-size variable)
        5. New root may violate max heap property, but its
        children are max heaps. Run max_heapify to fix this.
        6. Go to Step 2 unless heap is empty. 
        '''
        self.build_max_heap()
        for index in range(len(self._array), 0, -1):
            max_index = len(self._array)
            self.swap(0, index-1)
            self.max_heapify(0, index-1)

    def main(self, _array):
        '''main entry point'''
        self.set(_array)
        self.heap_sort()
        if self.verbosity:
            print('------------------------------------------')
            print(_array)

if __name__ == '__main__':
    HeapSort().run()