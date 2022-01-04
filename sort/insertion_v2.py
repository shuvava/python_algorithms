#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2017-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""Insertion sort(bubble sort)
Complexity: O(n^2)
for j(index) ← 2 to n
    insert key A[j] into the (already sorted) sub-array A[1 .. j-1].
by pairwise key-swaps down to its right position
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec03.pdf
"""
from typing import List


def sort(arr: List[int]) -> None:
    _len = len(arr)
    if _len < 2:
        return  # already sorted
    inx = 1
    while inx < _len:
        lkp = inx - 1
        tmp_inx: int = inx
        while lkp >= 0:
            if arr[tmp_inx] < arr[lkp]:
                arr[tmp_inx], arr[lkp] = arr[lkp], arr[tmp_inx]
                tmp_inx = lkp
            else:
                break
            lkp -= 1
        inx += 1


if __name__ == '__main__':
    _arr = [6, 5, 1, 4]
    sort(_arr)
    print(_arr)
