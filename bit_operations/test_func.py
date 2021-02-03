#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from func import get_mask, set_bit, get_bit, clear_bit, bit_count, \
    numberOfTrailingZeros, highestOneBit


class TestFunc(unittest.TestCase):
    def setUp(self):
        pass

    def test_read_file(self):
        result = get_mask(8)
        self.assertEqual(result, 255)

    def test_set_bit(self):
        val = set_bit(0, 0)
        val = set_bit(val, 1)
        val = set_bit(val, 2)
        self.assertEqual(val, 7)

    def test_clear_bit(self):
        val = clear_bit(7, 2)
        self.assertEqual(val, 3)

    def test_bit_count(self):
        res = bit_count(1_255_279_365)
        self.assertEqual(12, res)

    def test_numberOfTrailingZeros(self):
        res = numberOfTrailingZeros(381_344)
        self.assertEqual(5, res)

    def test_highestOneBit(self):
        res = highestOneBit(381_344)
        self.assertEqual(262_144, res)

    def test_get_bit(self):
        val = get_bit(7, 2)
        self.assertEqual(val, True)
        val = get_bit(8, 2)
        self.assertEqual(val, False)


if __name__ == '__main__':
    unittest.main()
