#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2017-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
Test of base_bst module
https://docs.python.org/3/library/unittest.html
'''
import os
import unittest

from file_operations import *


class Unit_test_file_operations(unittest.TestCase):
    def setUp(self):
        self.json_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../bst10.json'))
        self.array_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../test.txt'))

    def test_read_json_file(self):
        bst = read_json_file(self.json_file, 'bst', True)
        # print(bst)
        self.assertIsNotNone(bst)

    def test_read_array_file(self):
        arr = read_array_file(self.array_file, True)
        self.assertIsNotNone(arr)
        self.assertListEqual(arr, [[16, 4, 10, 14, 7, 9, 3, 2, 8, 1]])

    def test_save_json_file(self):
        tmp_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../test_bst10.json'))

        bst = read_json_file(self.json_file, 'bst')
        save_json_file(tmp_file, bst, 'bst', True)
        tmp_bst = read_json_file(tmp_file, 'bst')

        os.remove(tmp_file)
        self.assertIsNotNone(tmp_bst)
        self.assertDictEqual(bst, tmp_bst)

    def test_save_array_file(self):
        tmp_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../test_test.txt'))
        arr = read_array_file(self.array_file)
        save_array_file(tmp_file, arr, True)
        tmp_arr = read_array_file(tmp_file)

        os.remove(tmp_file)
        self.assertIsNotNone(tmp_arr)
        self.assertListEqual(arr, tmp_arr)


if __name__ == '__main__':
    unittest.main()
