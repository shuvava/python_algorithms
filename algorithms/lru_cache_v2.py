#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2020 Vladimir Shurygin.  All rights reserved.
#
"""
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU
https://github.com/python/cpython/blob/3.3/Lib/functools.py
"""
from collections import OrderedDict
from typing import List


class LRU(OrderedDict):
    """Limit size, evicting the least recently looked-up key when full"""

    def __init__(self, maxsize=128, /, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]


def test(s: List[int]) -> int:
    return 2


if __name__ == '__main__':
    test_cases = [
        ([1, 1, 1, 0, 1, 1, 1, 1], 2),
    ]
    cnt = 0
    for test_case in test_cases:
        params = test_case[:-1]
        expected = test_case[-1]
        actual = test(*params)
        is_correct = actual == expected
        cnt += 1
        print('.', end='')
        if not is_correct:
            print(f'\n{params} => (actual={actual}) != (expected={expected})')
    print(f'\nchecked {cnt} tests')
