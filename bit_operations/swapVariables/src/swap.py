#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2019-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
map arabic numbers to roman numbers
"""
import argparse
import random

MAX_VALUE = 2 ** 8 - 1


def get_max(val):
    max_val = 1
    iteration = 1
    while max_val < val:
        iteration += 1
        max_val *= 2
    return iteration


def swap(val1, val2):
    iteration = 0
    max_iteration = get_max(val1)
    print(f'max_iteration= {max_iteration}')
    for iteration in range(0, max_iteration):
        # print(f'iteration {iteration}')
        val2 = (val2 << 1 | ((val1 & 2 ** (max_iteration - 1)) >> (max_iteration - 1))) & (2 ** max_iteration - 1)
        # print(f'val2:{val2}({val2:#010b})')
        val1 = (((val1 & (2 ** max_iteration - 1)) << 1) | ((val2 & 2 ** (max_iteration - 1))) >> (
                max_iteration - 1)) & (2 ** max_iteration - 1)
        # print(f'val1:{val1}({val1:#010b})')
    val1 = val1 >> 1
    return (val1, val2)


def swap_binary(x, y):
    x = x ^ y;
    y = x ^ y;
    x = x ^ y;
    return (x, y)


def swap_summarize(x, y):
    x = x + y
    y = x - y
    x = x - y
    return (x, y)


def swap_main(val1, val2):
    if val1 > val2:
        return swap(val1, val2)
    _result = swap(val2, val1)
    return (_result[1], _result[0])


def get_context():
    ''' Create execution context command line args
    Returns
    -------
    Object
        object with command line arguments '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-n1", "--number1", \
                        help="sample number", \
                        dest="number1", type=int, default=random.randrange(1, MAX_VALUE))
    parser.add_argument("-n2", "--number2", \
                        help="sample number", \
                        dest="number2", type=int, default=random.randrange(1, MAX_VALUE))
    return parser.parse_args()


if __name__ == '__main__':
    context = get_context()
    number1 = context.number1
    number2 = context.number2
    print(f'number1:{number1}({number1:#010b}); number2:{number2}({number2:#010b})')
    # result = swap_main(number1, number2)
    # result = swap_binary(number1, number2)
    result = swap_summarize(number1, number2)
    number1 = result[0]
    number2 = result[1]
    print(f'number1:{number1}({number1:#010b}); number2:{number2}({number2:#010b})')
