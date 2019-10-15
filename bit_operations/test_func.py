#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from func import get_mask, set_bit, clear_bit

class TestFunc(unittest.TestCase):
    def setUp(self):
        pass

    def test_read_file(self):
        result = get_mask(8)
        self.assertEqual(result, 255)

    def test_set_bit(self):
        val = set_bit(0,0)
        val = set_bit(val,1)
        val = set_bit(val,2)
        self.assertEqual(val, 7)

    def test_clear_bit(self):
        val = clear_bit(7,2)
        self.assertEqual(val, 3)

if __name__ == '__main__':
    unittest.main()
