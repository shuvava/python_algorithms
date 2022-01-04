#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2020-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Heap's algorithm
https://en.wikipedia.org/wiki/Heap%27s_algorithm
https://www.baeldung.com/java-array-permutations
"""
from typing import List


def all_perms(elements: List[int]):
    n = len(elements)
    # c is an encoding of the stack state.
    c = [0] * n
    # i acts similarly to the stack pointer
    i = 0
    yield elements[:]
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                elements[i], elements[0] = elements[0], elements[i]
            else:
                elements[i], elements[c[i]] = elements[c[i]], elements[i]
            yield elements[:]
            c[i] += 1
            # Simulate recursive call reaching the base case
            # by bringing the pointer to the base case analog in the array
            i = 0
        else:
            # Reset the state and simulate popping
            # the stack by incrementing the pointer.
            c[i] = 0
            i += 1


def permute(nums: List[int]) -> List[List[int]]:
    result = []
    for s in all_perms(nums):
        result.append(s)
    return result


if __name__ == '__main__':
    data = [1, 2, 3]
    res = permute(data)
    print(res)
