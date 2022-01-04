#!/usr/bin/env python3
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2017-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
Test of base_bst module
https://docs.python.org/3/library/unittest.html
'''
import unittest

from radix import get_offset_code, sort

__print__ = False


class Unit_test_radix(unittest.TestCase):
    def setUp(self):
        pass

    def test_getOffsetCode_not_supported_range(self):
        _str = '$az'
        inx = get_offset_code(_str, 0)
        self.assertEqual(inx, 0, 'should be zero')
        inx = get_offset_code(_str, 10)
        self.assertEqual(inx, 0, 'should be zero')
        inx = get_offset_code(_str, 1)
        self.assertEqual(inx, 0, 'should be zero')
        inx = get_offset_code(_str, 2)
        self.assertEqual(inx, 0, 'should be zero')

    def test_min_max_supported_range(self):
        _str = 'AZ09'
        inx = get_offset_code(_str, 2)
        self.assertEqual(inx, 1, 'should be 1')
        inx = get_offset_code(_str, 3)
        self.assertEqual(inx, 10, 'should be 10')
        inx = get_offset_code(_str, 0)
        self.assertEqual(inx, 11, 'should be 11')
        inx = get_offset_code(_str, 1)
        self.assertEqual(inx, 36, 'should be 36')

    def test_sort(self):
        arr = ['Z1', 'Z0', 'A5', 'A7', '00', '$$']
        sorted_arr = sort(arr, len(arr))
        if __print__:
            print(sorted_arr)
        self.assertEqual(sorted_arr, ['$$', '00', 'A5', 'A7', 'Z0', 'Z1'])


if __name__ == '__main__':
    __print__ = True
    unittest.main()
