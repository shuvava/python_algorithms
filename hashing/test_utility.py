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
from utility import prehash

__print__ = False

class Unit_test_Prehash(unittest.TestCase):
    def setUp(self):
        pass

    def test_prehashing(self):
        #arrange
        test01 = 'Hello world!'
        test02 = 1;
        #act
        h01 = prehash(test01)
        h02 = prehash(test02)
        #assert
        self.assertIsInstance(h01, int)
        self.assertGreater(h01, 0, 'Should be greater zero')
        self.assertIsInstance(h02, int)
        self.assertGreater(h02, 0, 'Should be greater zero')

if __name__ == '__main__':
    __print__ = True
    unittest.main()