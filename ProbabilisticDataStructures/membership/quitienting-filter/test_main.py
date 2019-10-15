#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from random import Random

from main import QuotientFilter
from mock_hash_fn import hash_fn, mock

class TestQuotientFilter(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        b = QuotientFilter(3, 10, hash_fn)
        self.assertEqual(8, b.MAX_SIZE)

    def test_setitem(self):
        b = QuotientFilter(3, 10, hash_fn)
        b[0] = 1023
        res = b.table[0]
        self.assertEqual(1023, res)
        b[1] = 1023
        res = b.table[0]
        val = (1023 << 13)+1023
        self.assertEqual(val, res)

    def test_getitem(self):
        b = QuotientFilter(3, 10, hash_fn)
        res = []
        hasher = Random(0).randrange
        for i in range(7):
            val = hasher(1023)
            b[i] = val
            res.append(val)
        for i in range(7):
            self.assertEqual(b[i], res[i])

    def test_insert(self):
        b = QuotientFilter(3, 13, hash_fn)
        for key in mock.keys():
            b.insert(key)
        for key in mock.keys():
            self.assertTrue(key in b)
        #b.insert('Copenhagen')
        # b.insert('Lisbon')
        # b.insert('Paris')
        # b.insert('Stockholm')
        # b.insert('Zagreb')
        # b.insert('Warsaw')

        # res = 'Copenhagen' in b
        # self.assertTrue(res)

    def test_remove(self):
        b = QuotientFilter(3, 13, hash_fn)
        for key in mock.keys():
            b.insert(key)
        for key in mock.keys():
            del b[key]
            self.assertFalse(key in b)
        self.assertEqual(0, len(b))

if __name__ == '__main__':
    unittest.main()
