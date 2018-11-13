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

from heap_sort import HeapSort
from bst_heap_utils import get_array

__verbose__ = False
__stat__ = False

class UnitTestHeapSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_sort(self):
        #arrange
        arr = [5, 55, 93, 83, 55, 122, 72]
        #act
        heap = HeapSort(list(arr))
        heap.heap_sort()
        #assert
        _arr = arr.copy()
        _arr.sort()
        self.assertEqual(_arr, heap.array)
        pass


if __name__ == '__main__':
    __verbose__ = False
    __stat__ = False
    unittest.main()
