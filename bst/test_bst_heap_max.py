#!/usr/bin/env python3
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2017-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
Test of base_bst module
https://docs.python.org/3/library/unittest.html
'''
import cProfile
import pstats
import unittest

from bst_heap_max import MaxHeap
from bst_heap_utils import get_array, print_tree

__verbose__ = False
__stat__ = False


class UnitTestMaxHeap(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_array(self):
        arr = get_array(None, 10, __verbose__)
        self.assertIsNotNone(arr)

    def test_max_heap_init(self):
        arr = get_array(None, 10, __verbose__)
        heap = MaxHeap(arr)
        self.assertEqual(arr, heap.array)

    def test_max_heap_build(self):
        sortby = 'cumulative'
        pr = cProfile.Profile()
        # arrange
        arr = get_array(None, 5, __verbose__)
        # arr = [5, 55, 93, 83, 55, 122, 72, 58, 69, 18, 138, 19, 149, 47, 33]
        # act
        heap = MaxHeap(list(arr))
        pr.enable()
        heap.build_heap()
        pr.disable()
        if __verbose__:
            print_tree(heap)
        if __stat__:
            ps = pstats.Stats(pr).sort_stats(sortby)
            ps.print_stats()
            pr.clear()
        arr.sort(reverse=True)
        if __verbose__:
            print('arr={}'.format(arr))
        for inx in range(len(arr)):
            pr.enable()
            item = heap.pop()
            pr.disable()
            if __verbose__:
                print_tree(heap)
            if __stat__:
                print('inx={};len={}~~~~~~~~'.format(inx, len(heap.array)))
                ps = pstats.Stats(pr).sort_stats(sortby)
                ps.print_stats()
                pr.clear()
            # assert
            self.assertEqual(arr[inx], item)

    def test_heap_sort(self):
        # arrange
        arr = get_array(None, 10, __verbose__)
        # act
        heap = MaxHeap(list(arr))
        heap.build_heap()
        arr.sort(reverse=True)
        _arr = heap.get_sorted()
        # assert
        self.assertEqual(arr, _arr)

    def test_heap_update(self):
        # arrange
        # arr = get_array(None, 10, not __verbose__)
        arr = [5, 55, 93, 83, 55, 122, 72]
        # act
        heap = MaxHeap(list(arr))
        heap.build_heap()
        if __verbose__:
            print_tree(heap, with_ids=True)
        inx = int(len(heap.array) / 4)
        val = heap.array[inx]
        heap.update(inx, val * 3)
        _arr = heap.array.copy()
        _heap = MaxHeap(list(_arr))
        _heap.build_heap()
        if __verbose__:
            print_tree(heap)
        # assert
        self.assertEqual(heap.array, _heap.array)

    def test_heap_push(self):
        # arrange
        # arr = get_array(None, 10, not __verbose__)
        arr = [5, 55, 93, 83, 55, 122, 72]
        # act
        heap = MaxHeap(list(arr))
        heap.build_heap()
        if __verbose__:
            print_tree(heap, with_ids=True)
        heap.push(85)
        heap.push(87)
        if __verbose__:
            print_tree(heap)
        _arr = heap.array.copy()
        _heap = MaxHeap(list(_arr))
        _heap.build_heap()
        # assert
        self.assertEqual(heap.array, _heap.array)

    def test_heap_push_sequence(self):
        # arrange
        _len = 10
        arr = get_array(None, _len, __verbose__)
        # act
        heap = MaxHeap(list())
        for item in arr:
            heap.push(item)
        _heap = MaxHeap(list(arr))
        _heap.build_heap()
        if __verbose__:
            print_tree(heap)
            print_tree(_heap)
        # assert
        for i in range(_len):
            pop = heap.pop()
            _pop = _heap.pop()
            self.assertEqual(pop, _pop)


if __name__ == '__main__':
    __verbose__ = False
    __stat__ = False
    unittest.main()
