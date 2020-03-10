#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
"""
Test of base_bst module
https://docs.python.org/3/library/unittest.html
"""
import unittest

from rotation_juggling import leftRotate

__print__ = False


class UnitTestRotationJuggling(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_array_left_ratate(self):
        if __print__:
            print('--------------------test_array_left_ratate')
        # arrange
        arr = [1, 2, 3, 4, 5, 6, 7]
        #act
        leftRotate(arr, 2)
        if __print__:
            for i in range(len(arr)):
                print ("% d" % arr[i], end=" ")
        self.assertEqual(arr, [3, 4, 5, 6, 7, 1, 2])


if __name__ == '__main__':
    __print__ = True
    unittest.main()
