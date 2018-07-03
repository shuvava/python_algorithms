#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
Test of base_bst module
https://docs.python.org/3/library/unittest.html
'''
import unittest

import cProfile, pstats

from bst_heap_min import MinHeap
from bst_heap_utils import get_array, print_tree

__verbose__ = False
__stat__ = False

class UnitTestMinHeap(unittest.TestCase):
    def setUp(self):
        pass

    def test_min_heap_build(self):
        sortby = 'cumulative'
        pr = cProfile.Profile()
        #arrange
        arr = get_array(None, 15, __verbose__)
        #arr = [5, 55, 93, 83, 55, 122, 72, 58, 69, 18, 138, 19, 149, 47, 33]
        #act
        heap = MinHeap(list(arr))
        pr.enable()
        heap.build_heap()
        pr.disable()
        if __verbose__:
            print_tree(heap)
        if __stat__:
            ps = pstats.Stats(pr).sort_stats(sortby)
            ps.print_stats()
            pr.clear()
        arr.sort(reverse=False)
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
            #assert
            self.assertEqual(arr[inx], item)


if __name__ == '__main__':
    __verbose__ = False
    __stat__ = False
    unittest.main()
