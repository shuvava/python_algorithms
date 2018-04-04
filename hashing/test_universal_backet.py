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
from universal_backet import UniversalBasket

__print__ = False

class Unit_test_UniversalBasket(unittest.TestCase):
    def setUp(self):
        pass

    def test_incorrect_param(self):
        self.assertRaises(ValueError, UniversalBasket, 7,5)

    def test_multi_basket(self):
        #arrange
        test01 = 'Hello world!'
        test02 = 2
        h01 = prehash(test01)
        h02 = prehash(test02)
        basket = UniversalBasket(4)
        #act
        bs01 = basket.get_basket(h01)
        bs02 = basket.get_basket(h02)
        #assert
        self.assertNotEqual(bs01, bs02)

    def test_div_basket_worst_case(self):
        #arrange
        count = 4
        basket = UniversalBasket(4)
        test = [2]
        for i in range(1, count):
            test.append(test[i-1]*2)
        if __print__:
            print(test)
        #act
        bs = []
        for i in range(0, count):
            bs.append(basket.get_basket(test[i]))
        if __print__:
            print(bs)
        #assert
        duplicates = [[x, bs.count(x)] for x in set(bs) if bs.count(x) > 2]
        if __print__:
            print(duplicates)
        self.assertEqual(len(duplicates), 0)


if __name__ == '__main__':
    __print__ = True
    unittest.main()