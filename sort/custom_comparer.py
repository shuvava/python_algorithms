#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2021 Vladimir Shurygin.  All rights reserved.
#
"""
Custom comparer for sorting functions
"""

from functools import cmp_to_key
from typing import List, Callable


def create_verification_fn(letters: str) -> Callable[[str, str], int]:
    """custom list sort comparer method
    usage:
        >>> sorted(["cca", "ccbc", "ccbb"], key=cmp_to_key(create_verification_fn("abc")))
        ["cca", "ccbb", "ccbc"]
    """
    cache, _len = {}, len(letters)
    for i in range(_len):
        c = letters[i]
        cache[c] = i

    def compare(a: str, b: str) -> int:
        lena, lenb = len(a), len(b)
        _len = min(lena, lenb)
        for i in range(_len):
            ca, cb = a[i], b[i]
            if cache[ca] < cache[cb]:
                return -1
            elif cache[ca] > cache[cb]:
                return 1
            else:
                continue
        if lena < lenb:
            return -1
        elif lena > lenb:
            return 1
        else:
            return 0

    return compare


def test(arr: List[str], abc: str) -> List[str]:
    _compare = create_verification_fn(abc)
    return sorted(arr, key=cmp_to_key(_compare))


if __name__ == '__main__':
    test_cases = [
        (["wrt", "ett", "rftt", "wrf", "er"], "wertf", ["wrt", "wrf", "er", "ett", "rftt"]),
        (["x", "z"], "zx", ["z", "x"]),
        (["aac", "aaba", "aabb"], "cba", ["aac", "aabb", "aaba"]),
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
