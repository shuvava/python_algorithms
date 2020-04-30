#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2020 Vladimir Shurygin.  All rights reserved.
#
"""

"""
from typing import List


def get_pivot(nums: List[int]) -> int:
    low = 0
    high = len(nums) - 1
    while low < high:
        if low + 1 == high and nums[low] > nums[high]:
            return high
        mid = (high + low) >> 1
        if nums[mid] > nums[high]:
            low = mid
        else:
            high = mid
    return 0


if __name__ == '__main__':
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 4),
    ]
    cnt = 0
    for test_case in test_cases:
        params = test_case[:-1]
        expected = test_case[-1]
        actual = get_pivot(*params)
        is_correct = actual == expected
        cnt += 1
        print('.', end='')
        if not is_correct:
            print(f'\n{params} => (actual={actual}) != (expected={expected})')
    print(f'\nchecked {cnt} tests')
