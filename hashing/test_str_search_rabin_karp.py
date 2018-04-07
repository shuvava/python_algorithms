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

    def wrong_param_test(self):
        #arrange
        s = 'the'
        pattern = 'world'
        #act
        result = rabin_karp(s, pattern)
        #assert
        self.assertEqual(result, -1)
    
    def equal_test(self):
            #arrange
        s = 'the world'
        pattern = 'the'
        #act
        result = rabin_karp(s, pattern)
        #assert
        self.assertEqual(result, 1)

    def find_test(self):
            #arrange
        s = 'I love the world'
        pattern = 'the'
        #act
        result = rabin_karp(s, pattern)
        #assert
        self.assertEqual(result, 7)

    def not_found_test(self):
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
