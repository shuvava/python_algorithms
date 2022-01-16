#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Largest Triple Products
You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)]
such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the product of
the three largest elements out of arr[0..i] (or equal to -1 if i < 2, as arr[0..i] then includes fewer than three elements).
Note that the three largest elements used to form any product may have the same values as one another,
but they must be at different indices in arr.
Signature
    int[] findMaxProduct(int[] arr)
Input
    n is in the range [1, 100,000].
    Each value arr[i] is in the range [1, 1,000].
Output
    Return a list of n integers output[0..(n-1)], as described above.
Example 1
    n = 5
    arr = [1, 2, 3, 4, 5]
    output = [-1, -1, 6, 24, 60]
    The 3rd element of output is 3*2*1 = 6, the 4th is 4*3*2 = 24, and the 5th is 5*4*3 = 60.
Example 2
    n = 5
    arr = [2, 1, 2, 1, 2]
    output = [-1, -1, 4, 4, 8]
    The 3rd element of output is 2*2*1 = 4, the 4th is 2*2*1 = 4, and the 5th is 2*2*2 = 8.
"""
from typing import List

__all__ = ['heap_push']


def heap_push(heap: List[int], newitem: int):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(newitem)
    startpos, pos = 0, len(heap) - 1
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


def test(arr: List[int]) -> List[int]:
    heap, res = [], []
    for i in range(len(arr)):
        item = arr[i]
        heap_push(heap, item)
        if len(heap) < 3:
            res.append(-1)
        else:
            res.append(heap[-1] * heap[-2] * heap[-3])
    return res


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5], [-1, -1, 6, 24, 60]),
        ([2, 1, 2, 1, 2], [-1, -1, 4, 4, 8]),
        ([2, 4, 7, 1, 5, 3], [-1, -1, 56, 56, 140, 140]),
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
