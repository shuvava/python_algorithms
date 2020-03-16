#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2020 Vladimir Shurygin.  All rights reserved.
#
"""
Heap's algorithm
https://en.wikipedia.org/wiki/Heap%27s_algorithm
"""
from typing import List


def all_perms(elements: List[int], n: int):
    if n == 1:
        yield elements[:]
    else:
        for i in range(n-1):
            for hp in all_perms(elements, n-1):
                yield hp
            if n % 2 == 0:
                elements[i], elements[n-1] = elements[n-1], elements[i]
            else:
                elements[0], elements[n - 1] = elements[n - 1], elements[0]
        for hp in all_perms(elements, n - 1):
            yield hp


def permute(nums: List[int]) -> List[List[int]]:
    result = []
    for s in all_perms(nums, len(nums)):
        result.append(s)
    return result


if __name__ == '__main__':
    data = [1, 2, 3]
    res = permute(data)
    print(res)
