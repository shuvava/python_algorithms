#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom iterator example
taken from https://www.ics.uci.edu/~pattis/ICS-33/lectures/disassembly.txt
"""
import dis

__author__ = 'Vladimir Shurygin'
__copyright__ = 'Copyright 2019, Algorithms'
__version__ = '0.0.1'
__status__ = 'dev'


def addup(alist):
    sum = 0
    for v in alist:
        sum = sum + v
    return sum


def func_obj(fo):
    print(fo.__name__)
    print('  co_varnames:', fo.__code__.co_varnames)
    print('  co_names   :', fo.__code__.co_names)
    print('  co_consts  :', fo.__code__.co_consts, '\n')
    print('Source Line  m  operation/byte-code      operand (useful name/number)\n' + 69 * '-')
    dis.dis(fo)


if __name__ == '__main__':
    func_obj(addup)
