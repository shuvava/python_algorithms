#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
"""
Find the contiguous subarray within an array
(containing at least one number) which has the largest sum.

For example given the array [-2, 1,-3, 4, -1, 2, 1, -5, 4],
the contiguous subarray [4, -1, 2, 1] has the largest sum = 6.

Complexity O(n)
"""


def kadane(arr):
    max_current = max_global = arr[0]
    _len = len(arr)
    for i in range(1, _len):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global


if __name__ == '__main__':
    _arr = [-100, -2, 3, 2, -1]
    res = kadane(_arr)
    print(f'res={res} should be 5')
    _arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = kadane(_arr)
    print(f'res={res} should be 6')
