#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2020 Vladimir Shurygin.  All rights reserved.
#
"""
insert new element into sorted array
with maintaining sorting
original https://github.com/python/cpython/blob/3.7/Lib/bisect.py

complexity O(ln(n))
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    _len = len(nums)
    low = 0
    high = _len - 1
    while low <= high:
        mid: int = ((high + low) >> 1)
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    test_cases = [
        ([1, 3, 5, 9], 9, 3),
        ([1, 3, 5, 9], 5, 2),
    ]
    cnt = 0
    for test_case in test_cases:
        params = test_case[:-1]
        expected = test_case[-1]
        actual = search(*params)
        is_correct = actual == expected
        cnt += 1
        print('.', end='')
        if not is_correct:
            print(f'\n{params} => (actual={actual}) != (expected={expected})')
    print(f'\nchecked {cnt} tests')
