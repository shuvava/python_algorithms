#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from random import Random

from bit_oprs_helper import bit_count
from linear_counting import LinearCounting

class TestLinearCounting(unittest.TestCase):
    def setUp(self):
        self.test_set = [
            'Berlin', ' Berlin', ' Paris', ' Berlin', ' Lisbon', ' Kiev',
            ' Paris', ' London', ' Rome', ' Athens', ' Madrid', ' Vienna',
            ' Rome', ' Rome', ' Lisbon', ' Berlin', ' Paris', ' London',
            ' Kiev', ' Washington'
        ]

    def test_add(self):
        lc = LinearCounting(16)
        lc.add(self.test_set[0])
        lc.add(self.test_set[2])
        self.assertEqual(2, bit_count(lc.table[0]))

    def test_count(self):
        lc = LinearCounting(16)
        for val in self.test_set:
            lc.add(val)
        self.assertLess(abs(10 - len(lc)), 3)

if __name__ == '__main__':
    unittest.main()
