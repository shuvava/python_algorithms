#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from random import Random

from stochastic_averaging import StochasticAveraging, rank, left_most_zero

class TestStochasticAveraging(unittest.TestCase):
    def setUp(self):
        pass

    def test_rank(self):
        test_cases = [
            (42, 1),
            (309000, 3)
        ]
        for val, expected in test_cases:
            with self.subTest(val=val, expected=expected):
                _rank = rank(val)
                self.assertAlmostEqual(expected, _rank)

    def test_left_most_zero(self):
        test_cases = [
            ([0xFFFFFFFF], None, 'all ones'),
            ([13], 1, 'not first'),
            ([23], 3, 'not first'),
            ([62], 0, 'first'),
            ([0xFFFFFFFF, 5], 32, 'all ones'),
            ]
        for val, expected, msg in test_cases:
            with self.subTest(val=val, expected=expected):
                res = left_most_zero(val)
                self.assertEqual(expected, res, msg)

    def test_cardinality(self):
        test_case = [
            'Athens', 'Berlin', 'Kiev', 'Lisbon', 'London', 'Madrid', 'Paris',
            'Rome', 'Vienna', 'Washington'
        ]
        srv = StochasticAveraging(3, 1)
        for item in test_case:
            srv.add(item)
        res = len(srv)
        expected = len(test_case)
        self.assertLess(res, expected*2)

    def test_create(self):
        test_cases = [
            (10**9, 0.097, 64, 32),
            (10**9, 0.0487, 256, 32),
            (10**9, 0.024, 1056, 32)
        ]
        for num_elm, error_rate, counter_cnt, filter_size in test_cases:
            with self.subTest(num_elm=num_elm, error_rate=error_rate):
                srv = StochasticAveraging.create(num_elm, error_rate)
                self.assertEqual(counter_cnt, srv.num_of_counters)
                self.assertEqual(filter_size, srv.filter_size)

    def test_cardinality2(self):
        arr = []
        cnt_set = set()
        num_elm = 10_000
        error_rate = 0.024
        hasher = Random(5).randrange
        for _ in range(num_elm):
            h = hasher(1000)
            arr.append(h)
            cnt_set.add(h)
        srv = StochasticAveraging.create(num_elm*100, error_rate)
        srv.with_small_cardinality_correction = 1
        for item in arr:
            srv.add(str(item))
        res = len(srv)
        expected = len(cnt_set)
        # self.assertLess(abs((expected-res)/expected), error_rate)


if __name__ == '__main__':
    unittest.main()
