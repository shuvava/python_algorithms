#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
#
'''
Given two integers, write a function to determine whether or not their binary representations differ by a single bit.
'''
import argparse
import random

MAX_VALUE = 2 ** 8 -1

def gray(n1, n2):
    xor = n1 ^ n2
    print(f'xor:{xor}({xor:#010b});')
    while xor > 0:
        if xor & 1 == 1 and xor >> 1 > 0:
            return False
        xor = xor >> 1
    return True

def get_context():
    ''' Create execution context command line args
    Returns
    -------
    Object
        object with command line arguments '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-n1", "--number1",\
        help="sample number",\
        dest="number1", type=int, default=random.randrange(1, MAX_VALUE))
    parser.add_argument("-n2", "--number2",\
        help="sample number",\
        dest="number2", type=int, default=random.randrange(1, MAX_VALUE))
    return parser.parse_args()

if __name__ == '__main__':
    context = get_context()
    number1 = context.number1
    number2 = context.number2
    print(f'number1:{number1}({number1:#010b}); number2:{number2}({number2:#010b})')
    result = gray(number1, number2)
    print(f'gray({number1}, {number2}) = {result}')
