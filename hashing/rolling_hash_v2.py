#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2020 Vladimir Shurygin.  All rights reserved.
#
"""
Implementation of Rabin-Karp algorithm
"""

BASE = 26
PRIME = 2 ** 63 - 1  # hashing.utility.findLargestPrimeFactor(BASE) -> 23 - also possible prime for base == 26


def test(s: str, to_find: str) -> bool:
    _len = len(s)
    lent = len(to_find)
    if lent > _len:
        return False
    target = 0
    for c in to_find:  # build target hash
        val = ord(c) - ord('a')
        target = (target * BASE + val) % PRIME
    cur_hash = 0
    for i in range(lent):  # initiate string hash
        val = ord(s[i]) - ord('a')
        cur_hash = (cur_hash * BASE + val) % PRIME
    if cur_hash == target:
        return True
    max_pow = pow(BASE, lent, PRIME)
    for i in range(lent, _len):
        val = ord(s[i]) - ord('a')
        old_val = ord(s[i - lent]) - ord('a')
        cur_hash = (cur_hash * BASE - old_val * max_pow + val) % PRIME
        if cur_hash == target:
            return True
    return False


if __name__ == '__main__':
    test_cases = [
        ("anaba", "ana", True),
        ("banana", "ana", True),
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
