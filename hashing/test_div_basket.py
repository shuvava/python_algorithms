#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2017-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
Test of base_bst module
https://docs.python.org/3/library/unittest.html
'''
import unittest

from div_basket import get_basket_div_method
from utility import prehash

__print__ = False


class Unit_test_Basketing(unittest.TestCase):
    def setUp(self):
        pass

    def test_div_basket(self):
        # arrange
        test01 = 'Hello world!'
        test02 = 1
        h01 = prehash(test01)
        h02 = prehash(test02)
        # act
        bs01 = get_basket_div_method(h01, 4)
        bs02 = get_basket_div_method(h02, 4)
        # assert
        self.assertNotEqual(bs01, bs02)

    def test_div_basket_worst_case(self):
        # arrange
        count = 4
        test = [2]
        for i in range(1, count):
            test.append(test[i - 1] * 2)
        if __print__:
            print(test)
        # act
        bs = []
        for i in range(0, count):
            bs.append(get_basket_div_method(test[i], 4))
        if __print__:
            print(bs)
        # assert
        duplicates = [[x, bs.count(x)] for x in set(bs) if bs.count(x) > 2]
        if __print__:
            print(duplicates)
        self.assertGreater(len(duplicates), 0, 'we should have duplicates')


if __name__ == '__main__':
    __print__ = True
    unittest.main()
