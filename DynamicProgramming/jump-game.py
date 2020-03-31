#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2020 Vladimir Shurygin.  All rights reserved.
#
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


def canJump(nums: List[int]) -> bool:
    """DP - dynamic programming algorithm from comment"""
    _len = len(nums)
    state = [False] * _len
    state[0] = True
    for i in range(1, _len):
        for j in range(i):
            if state[j] and j + nums[j] >= i:
                state[i] = True
    return state[_len - 1]


def can_jump(nums: List[int]) -> bool:
    """greedy algorithm"""
    _len = len(nums)
    state = [False] * _len
    state[0] = True
    for i in range(_len):
        if state[i]:
            val = nums[i]
            for j in (1, val + 1):
                inx = i + j
                if inx >= _len - 1:
                    return True
                if nums[inx] > 0:
                    state[inx] = True
    return state[_len - 1]


if __name__ == '__main__':
    # test_case =[2, 2, 3, 10, 1, 0, 0, 0, 0]
    # test_case =[1, 2, 0, 1]
    # test_case =[2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    test_case = [2, 5, 0, 0]  # true
    res1 = can_jump(test_case)
    res2 = canJump(test_case)
    print(f'{res1 == res2} => res = {res1}')
