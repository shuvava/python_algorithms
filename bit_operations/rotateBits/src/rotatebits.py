#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2019-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Given a number, write a function to rotate the bits (ie circular shift).
"""
import argparse
import random

MAX_BIT = 8
MAX_VALUE = 2 ** MAX_BIT - 1


def get_max(val):
    iteration = 0
    while val > 0:
        iteration += 1
        val = val >> 1
    return iteration


def rotate(n, r):
    max_iteration = get_max(n)
    for iteration in range(0, r):
        n = (n << 1 | ((n & 2 ** (max_iteration - 1)) >> max_iteration - 1)) & 2 ** max_iteration - 1
    return n


def get_context():
    """ Create execution context command line args
    Returns
    -------
    Object
        object with command line arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number",
                        help="sample number",
                        dest="number", type=int, default=random.randrange(1, MAX_VALUE))
    parser.add_argument("-r", "--rotate",
                        help="rotate bits",
                        dest="rotate", type=int, default=random.randrange(1, MAX_BIT))
    return parser.parse_args()


if __name__ == '__main__':
    context = get_context()
    n = context.number
    r = context.rotate
    result = rotate(n, r)
    print(f'rotate({n}[{n:#010b}], {r})={result}[{result:#010b}]')
