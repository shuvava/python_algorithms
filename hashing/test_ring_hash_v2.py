#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
#
from unittest import TestCase

from hashing.ring_hash_v2 import RingHash, NODE_ID


class UnitTestRingHashV2(TestCase):
    def setUp(self):
        pass

    def test_next(self):
        _hash = RingHash([3, 6, 9], 1, lambda key: int(str(key).split('-')[0]))
        r1 = _hash.get(2)
        r2 = _hash.get(10)
        r3 = _hash.get(4)
        # assert
        self.assertEqual(r1, 3, 'r1')
        self.assertEqual(r2, 3, 'r2')
        self.assertEqual(r3, 6, 'r3')

    def test_del_node(self):
        _hash = RingHash([3, 6, 9], 1, lambda key: int(str(key).split('-')[0]))
        node = _hash.remove(6)
        self.assertEqual(node[NODE_ID], 6)
        self.assertEqual(len(_hash), 2)
