#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
#
"""
Given an integer n, write a function to compute the nth Fibonacci number.
"""
import argparse
import random


def fibonacci(n):
    """it is naive implementation which takes exponential time to execute.
    BigO=2**(n/2)
    """
    if n <= 1:
        return 1
    n0 = 0
    n1 = 1
    result = 1
    level = 2
    while level <= n:
        result = n0 + n1
        n0 = n1
        n1 = result
        level += 1
    return result


_MEMO = {}


def fibonacci_with_hash(n):
    """
    it use memoize dynamic programming algorithm
    BigO = n
    """
    if n in _MEMO:
        return _MEMO[n]
    if n <= 2:
        return 1
    f = fibonacci_with_hash(n - 1) + fibonacci_with_hash(n - 2)
    _MEMO[n] = f
    return f


def fib_bottom_up(n):
    """
    dynamic programming bottom-up algorithm
    idea of algorithm is start solving program from bottom and go up,
    may uses in junction with memoize DP
    it use array as a cache
    BigO = n
    """
    _memo = [1] * n  # init array
    fib = 1
    for arr_inx in range(0, n):
        if arr_inx <= 1:
            fib = 1
        else:
            fib = _memo[arr_inx - 1] + _memo[arr_inx - 2]
        _memo[arr_inx] = fib
    return fib


def get_context():
    """ Create execution context command line args
    Returns
    -------
    Object
        object with command line arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number",
                        help="fibonacci level",
                        dest="number", type=int, default=random.randrange(0, 24))
    return parser.parse_args()


if __name__ == '__main__':
    context = get_context()
    level = context.number
    result = fibonacci(level)
    print(f'fibonacci({level}) = {result}')
    result = fib_bottom_up(level)
    print(f'fibonacci({level}) = {result}')
