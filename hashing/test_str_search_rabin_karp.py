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
from str_search_rabin_karp import rabin_karp

__print__ = False

class Unit_test_RabinKarp(unittest.TestCase):
    def setUp(self):
        pass

    def test_wrong_param(self):
        #arrange
        s = 'the'
        pattern = 'world'
        #act
        result = rabin_karp(s, pattern)
        #assert
        self.assertEqual(result, -1)
    
    def test_equal(self):
        #arrange
        s = 'the world'
        pattern = 'the'
        #act
        result = rabin_karp(s, pattern)
        #assert
        self.assertEqual(result, 0)

    def test_find(self):
        #arrange
        #s = 'uthe world'
        s = 'I love the world'
        pattern = 'the'
        #act
        result = rabin_karp(s, pattern)
        #assert
        self.assertEqual(result, 7)

    def test_not_found(self):
            #arrange
        s = 'I love the world'
        pattern = 'the1'
        #act
        result = rabin_karp(s, pattern)
        #assert
        self.assertEqual(result, -1)

if __name__ == '__main__':
    __print__ = True
    unittest.main()
