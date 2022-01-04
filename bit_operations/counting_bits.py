#!/usr/bin/env python
# encoding: utf-8

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ (c) 2020 Vladimir Shurygin.  All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
calculate the number of 1's in their binary representation and return them as an array.

Example 1:
    Input: 2
    Output: [0,1,1]
Example 2:
    Input: 5
    Output: [0,1,1,2,1,2]

We can have different transition functions, as long as x' is smaller than x and their pop counts have a function.

Algorithm
Following the same principle of the previous approach, we can also have a transition
function by playing with the least significant bit.
Let look at the relation between x and x' = x / 2x
x =  (1001011101)_2 = 605
x' = (100101110)_2 = 302


We can see that x' is differ than xx by one bit, because x'
 can be considered as the result of removing the least significant bit of x.
Thus, we have the following transition function of pop count P(x):
P(x)=P(x/2)+(x mod 2)
"""
from typing import List


def test(num: int) -> List[int]:
    ans = [0] * (num + 1)
    for i in range(1, num + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans


if __name__ == '__main__':
    test_cases = [
        (5, [0, 1, 1, 2, 1, 2]),
        (2, [0, 1, 1]),
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
