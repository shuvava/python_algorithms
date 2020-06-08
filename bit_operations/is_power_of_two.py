#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2020 Vladimir Shurygin.  All rights reserved.
#
"""
Given an integer, write a function to determine if it is a power of two.

Intuition
The idea behind both solutions will be the same: a power of two in binary representation is one 1-bit, followed by some zeros:

1 = (00000001)
2 = (00000010)
4 = (00000100)
8 = (00001000)

A number which is not a power of two, has more than one 1-bit in its binary representation:

3 = (00000011)
5 = (00000101)
6 = (00000110)
7 = (00000111)

The only exception is 0, which should be treated separately.
"""


def test(n: int) -> bool:
    if n == 0:
        return False
    return n & (-n) == n


if __name__ == '__main__':
    test_cases = [
        (218, False),
        (16, True),
        (1, True),
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
