#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
"""Merge sort
Complexity: O(n*ln(n))
require double size of memory
Algorithm:
1. Split array on a half (merge_sort) recursively till 1 elements array
2. merge two pre sorted sub array (merge) (on the deepest level array contents just one element)
"""


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)

        # This is where we optimize for best case.
        if arr[mid] > arr[mid + 1]:
            merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    i = low
    j = mid + 1
    k = 0
    temp = [0] * (high - low + 1)
    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while j <= high:  # if( i>mid )
        temp[k] = arr[j]
        k += 1
        j += 1
    while i <= mid:  # j>high
        temp[k] = arr[i]
        k += 1
        i += 1
    i = low
    for k in range(high - low + 1):
        arr[i] = temp[k]
        i += 1


if __name__ == '__main__':
    arr = [2, 1, 3, 1, 2]
    res = arr.copy()
    merge_sort(res, 0, len(arr) - 1)
    origin = sorted(arr)
    print(f'origin={origin} res={res}')
