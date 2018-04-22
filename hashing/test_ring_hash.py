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
from ring_hash import RingHash

__print__ = False

class Unit_test_RingHash(unittest.TestCase):
    def setUp(self):
        pass

    def test_next(self):
        #arrange
        rhash = RingHash(2)
        rhash._ring_hash = [3, 6, 9]
        #act
        r1 = rhash._GetNextShard(2)
        r2 = rhash._GetNextShard(10)
        r3 = rhash._GetNextShard(4)
        #assert
        self.assertEqual(r1, 3)
        self.assertEqual(r2, 3)
        self.assertEqual(r3, 6)
    
    def test_prev(self):
        #arrange
        rhash = RingHash(2)
        rhash._ring_hash = [3, 6, 9]
        #act
        r1 = rhash._GetPrevShard(2)
        r2 = rhash._GetPrevShard(10)
        r3 = rhash._GetPrevShard(4)
        #assert
        self.assertEqual(r1, 9)
        self.assertEqual(r2, 9)
        self.assertEqual(r3, 3)

if __name__ == '__main__':
    __print__ = True
    unittest.main()
