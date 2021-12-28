#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2021 Vladimir Shurygin.  All rights reserved.
#
"""
append element to sorted list
"""
from bisect import insort
from typing import List


def test_builtin(a: List[int], b: int) -> List[int]:
    """O(n)"""
    insort(a, b)
    return a


def test(a: List[int], x: int, reverse: bool) -> List[int]:
    lo, hi = 0, len(a)
    while lo < hi:  # O(log n)
        mid = (lo + hi) >> 1
        if reverse:  # if array is revers sorted (ie 5, 4, 3)
            if x > a[mid]:
                hi = mid
            else:
                lo = mid + 1
        else:  # if array is sorted in ascending order
            if x < a[mid]:
                hi = mid
            else:
                lo = mid + 1
    a.insert(lo, x)  # O(n)
    return a


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 4, 5], 3, False, [1, 2, 3, 4, 5]),
        ([2, 3, 4, 5], 1, False, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4], 5, False, [1, 2, 3, 4, 5]),
        ([5, 4, 2, 1], 3, True, [5, 4, 3, 2, 1]),
        ([5, 4, 3, 2], 1, True, [5, 4, 3, 2, 1]),
        ([4, 3, 2, 1], 5, True, [5, 4, 3, 2, 1]),
        ([], 5, True, [5]),
        ([], 5, False, [5]),
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
