#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
insert new element into sorted array
with maintaining sorting
original https://github.com/python/cpython/blob/3.7/Lib/bisect.py

complexity O(ln(n))
"""
__author__ = 'Vladimir Shurygin'
__copyright__ = 'Copyright 2019, Algorithms'
__version__ = '0.0.1'
__status__ = 'dev'


def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == '__main__':
    arr = [15, 12, 10]
    arr.sort()
    print(arr)
    res = bisect_right(arr, 13)
    print(f'res={res} arr={arr[:res]}')
