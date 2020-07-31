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
from collections import namedtuple
from typing import Dict, Optional, List, Any

PREV, NEXT, KEY, RESULT = 0, 1, 2, 3  # names for the link fields

Node = namedtuple('Node', ['prev', 'next', 'key', 'value'])


class LRUCache:
    cache: Dict[int, int]

    def __init__(self, capacity: int):
        """not thread safe implementation"""
        self.cache = {}
        self.maxsize = capacity
        self.hits = 0
        self.misses = 0
        self.full = False
        self.cache_get = self.cache.get  # bound method to lookup a key or return None
        # root of the circular doubly linked list
        self.root = []
        # initialize by pointing to self
        self.root[:] = [self.root, self.root, None, None]

    def _get(self, key: int) -> Optional[List[Any]]:
        link = self.cache_get(key)
        if link is not None:
            # Move the link to the front of the circular queue
            link_prev, link_next, _key, result = link
            link_prev[NEXT] = link_next
            link_next[PREV] = link_prev
            last = self.root[PREV]
            last[NEXT] = self.root[PREV] = link
            link[PREV] = last
            link[NEXT] = self.root
            self.hits += 1
            return link
        else:
            self.misses += 1
            return None

    def get(self, key: int) -> int:
        link = self._get(key)
        if link is not None:
            return link[RESULT]
        else:
            return -1  # Not Found

    def put(self, key: int, value: int) -> None:
        link = self._get(key)
        if link is not None:
            link[RESULT] = value
            self.get(key)
            return
        if self.full:
            # Use the old root to store the new key and result.
            oldroot = self.root
            oldroot[KEY] = key
            oldroot[RESULT] = value
            # Empty the oldest link and make it the new root.
            self.root = oldroot[NEXT]
            oldkey = self.root[KEY]
            self.root[KEY] = self.root[RESULT] = None
            # Now update the cache dictionary.
            del self.cache[oldkey]
            # Save the potentially reentrant cache[key] assignment
            # for last, after the root and links have been put in
            # a consistent state.
            self.cache[key] = oldroot
        else:
            # Put result in a new link at the front of the queue.
            last = self.root[PREV]
            link = [last, self.root, key, value]
            last[NEXT] = self.root[PREV] = self.cache[key] = link
            self.full = (len(self.cache) >= self.maxsize)
        self.misses += 1
        return None


if __name__ == '__main__':
    test_cases = [
        (2, [2], [2, 6], [1], [1, 5], [1, 2], [1], [2], [-1, None, -1, None, None, 2, 6]),
        (2, [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4], [None, None, 1, None, -1, None, -1, 3, 4]),
    ]
    cnt = 0
    for test_case in test_cases:
        cache = LRUCache(test_case[0])
        params = test_case[1:-1]
        expected = test_case[-1]
        actual = []
        for item in params:
            if len(item) == 2:
                actual.append(cache.put(item[0], item[1]))
            else:
                actual.append(cache.get(item[0]))
        is_correct = actual == expected
        cnt += 1
        print('.', end='')
        if not is_correct:
            print(f'\n{params} => (actual={actual}) != (expected={expected})')
    print(f'\nchecked {cnt} tests')
