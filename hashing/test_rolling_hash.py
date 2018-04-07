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
from rolling_hash import PolynomialRollingHash

__print__ = False

class Unit_test_MultiBasket(unittest.TestCase):
    def setUp(self):
        pass

    def test_rolling_hash_init(self):
        #arrange
        str1 = 'abr'
        str2 = 'abr'
        hash1 = PolynomialRollingHash(256)
        hash2 = PolynomialRollingHash(256)
        #act
        for c in str2:
            hash2.add_symbol(c)
        for c in str1:
            hash1.add_symbol(c)
        #assert
        self.assertEqual(hash1.hash, hash2.hash)

    def test_rolling_hash_remove_zero(self):
        #arrange
        str1 = 'a'
        hash1 = PolynomialRollingHash(256)
        #act
        hash1.add_symbol('a')
        hash1.remove()
        #assert
        self.assertEqual(hash1.hash, 0)

    def test_rolling_hash_remove_one_symbol(self):
        #arrange
        str1 = 'ab'
        hash1 = PolynomialRollingHash(256)
        hash2 = PolynomialRollingHash(256)
        #act
        for c in str1:
            hash1.add_symbol(c)
        hash1.remove()
        #assert
        self.assertEqual(hash1.hash, ord('b'))

    def test_rolling_hash_remove(self):
        #arrange
        str1 = 'bra'
        str2 = 'abr'
        hash1 = PolynomialRollingHash(256)
        hash2 = PolynomialRollingHash(256)
        #act
        for c in str1:
            hash1.add_symbol(c)
        for c in str2:
            hash2.add_symbol(c)
        hash2.remove()
        hash2.add_symbol('a')
        #assert
        self.assertEqual(hash1.hash, hash2.hash)

    def test_rolling_hash_shift(self):
        #arrange
        str1 = 'bra'
        str2 = 'abr'
        hash1 = PolynomialRollingHash(256)
        hash2 = PolynomialRollingHash(256)
        #act
        for c in str1:
            hash1.add_symbol(c)
        for c in str2:
            hash2.add_symbol(c)
        hash2.shift_symbol('a')
        #assert
        self.assertEqual(hash1.hash, hash2.hash)

if __name__ == '__main__':
    __print__ = True
    unittest.main()
