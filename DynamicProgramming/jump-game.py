#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2020-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""
from typing import List


def can_jump(nums: List[int]) -> bool:
    """greedy algorithm"""
    _len = len(nums)
    state = [False] * _len
    state[0] = True
    for i in range(_len):
        if state[i]:
            val = nums[i]
            if i + val >= _len - 1:
                return True
            state[i + 1:i + 1 + val] = [True] * val
    return state[_len - 1]


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], True),
        ([3, 2, 1, 0, 4], False),
        ([2, 0], True),
        ([2, 5, 0, 0], True),
    ]
    cnt = 0
    for test_case in test_cases:
        params = test_case[:-1]
        expected = test_case[-1]
        actual = can_jump(*params)
        is_correct = actual == expected
        cnt += 1
        print('.', end='')
        if not is_correct:
            print(f'\n{params} => (actual={actual}) != (expected={expected})')
    print(f'\nchecked {cnt} tests')
