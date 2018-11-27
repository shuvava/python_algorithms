#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
'''
from rolling_hash import PolynomialRollingHash

def rabin_karp(s, pattern):
    '''
    s - string where search
    pattern - string to search
    '''
    if len(s) < len(pattern):
        return -1
    phash = PolynomialRollingHash(256)
    shash = PolynomialRollingHash(256)
    inx = 0
    for c in pattern:
        phash.add_symbol(c)
    for c in s[:len(pattern)]:
        shash.add_symbol(c)
    if shash.hash == phash.hash:
        if s[:len(pattern)] == pattern:
            return inx
    for c in s[len(pattern)+1:]:
        inx += 1
        shash.shift_symbol(s[len(pattern) + inx-1])
        if shash.hash == phash.hash:
            if s[inx:len(pattern) + inx] == pattern:
                return inx
    return -1
