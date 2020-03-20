#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
"""
Time complexity : O(n)

implementation of "A Juggling Algorithm" of array rotation
Instead of moving one by one, divide the array in different sets
where number of sets is equal to GCD of n and d and move the elements within sets.

GCD - greatest common divisor

If GCD is 1 as is for the above example array (n = 7 and d =2),
then elements will be moved within one set only,
we just start with temp = arr[0] and keep moving arr[I+d] to arr[I]
and finally store temp at the right place.
"""


def gcd(a, b):
    """find greatest common divisor of a and b
    Parameters
    ----------
        a: int - number
        b: int - number
    Returns
    -------
        int - greatest common divisor
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def leftRotate(arr, num_elm):
    """left rotate arr[] by num_elm
    Parameters
    ----------
        arr: list - array to rotate
        num_elm: int - number of element to rotate
    """
    size = len(arr)
    _gdc = gcd(num_elm, size)
    for iter_num in range(_gdc):
        # move i-th values of blocks
        temp = arr[iter_num]
        inx_start = iter_num
        while 1:
            inx = inx_start + num_elm
            if inx >= size:
                inx = inx - size
            if inx == iter_num:
                break
            arr[inx_start] = arr[inx]
            inx_start = inx
        arr[inx_start] = temp
