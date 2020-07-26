#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
#
"""QuickSort
Complexity: O(n*ln(n)); Worst: O(n2)
Algorithm:
    1. Partition array -> choose pivot element
         put in the left array elements smaller pivot
         put in the left array elements bigger pivot
"""
from typing import List


def partition(a: List[int], start_inx: int, end_inx: int) -> int:
    """Rearranges the elements of array[start:end] so that every element in
        array[start:pivot] is less than or equal to array[pivot] and every element in
        array[pivot:end] is greater than array[pivot]. Returns the index pivot to the caller
    """
    pivot = inx = start_inx
    while inx < end_inx:
        if a[inx] <= a[end_inx]:
            a[pivot], a[inx] = a[inx], a[pivot]
            pivot += 1
        inx += 1
    a[pivot], a[end_inx] = a[end_inx], a[pivot]
    return pivot


def quicksort(A: List[int], start_inx: int, end_inx: int) -> List[int]:
    if end_inx <= start_inx:
        return
    middle = partition(A, start_inx, end_inx)
    quicksort(A, start_inx, middle - 1)
    quicksort(A, middle + 1, end_inx)
    return A


if __name__ == '__main__':
    arr = [6, 5, 3, 2, 8, 10, 9]
    print(arr)
    result = quicksort(arr, 0, len(arr) - 1)
    print(result)
