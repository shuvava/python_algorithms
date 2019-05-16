#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''Merge sort
Complexity: O(n*ln(n))
require double size of memory
Algorithm:
1. Split array on a half (merge_sort) recursively till 1 elements array
2. merge two pre sorted sub array (merge) (on the deepest level array contents just one element)
'''

def merge(a1, a2):
    i, j, result, m, n = 0, 0, [], len(a1), len(a2)
    ra = result.append
    while i < m and j < n:
        if a1[i] <= a2[j]:
            ra(a1[i])
            i += 1
        else:
            ra(a2[j])
            j += 1
    result += a1[i:]
    result += a2[j:]
    return result

def merge_sort(arr):
    '''most optimal on python implementation of merge sort
    the same memory usage as for v2
    '''
    n = len(arr)
    mid = n // 2
    if n > 1:
        left_result = merge_sort(arr[:mid])
        right_result = merge_sort(arr[mid:])
        result = merge(left_result, right_result)
        return result
    return arr

if __name__ == '__main__':
    arr = [2, 1, 3, 1, 2]
    res = merge_sort(arr.copy())
    origin = sorted(arr)
    print(f'origin={origin} res={res}')
