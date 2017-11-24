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
import os
from sys import path

from file_operations import read_json_file, save_json_file

class Unit_test_file_operations(unittest.TestCase):

    def test_read_file(self):
        file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../bst10.json'))
        bst = read_json_file(file, 'bst', True)
        print(bst)
        self.assertIsNotNone(bst)

    def test_save_file(self):
        file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../bst10.json'))
        tmp_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../test_bst10.json'))

        bst = read_json_file(file, 'bst')
        save_json_file(tmp_file, bst, 'bst', True)
        tmp_bst = read_json_file(tmp_file, 'bst')

        os.remove(tmp_file)
        self.assertIsNotNone(tmp_bst)
        self.assertDictEqual(bst, tmp_bst)

if __name__ == '__main__':
    unittest.main()
