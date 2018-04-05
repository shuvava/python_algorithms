#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
Implementation of Rolling hash function
https://en.wikipedia.org/wiki/Rolling_hash
https://www.geeksforgeeks.org/searching-for-patterns-set-3-rabin-karp-algorithm/
https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
'''
from utility import findLargestPrimeFactor

class PolynomialRollingHash:
    '''
    Polynomial rolling hash
    H = C1*a^(k-1)+C2*a^(k-2)+...Ck*a^(0)

    where 
        C1..Ck - ASII code of string
        k      - max length of string
    
    In order to avoid manipulating huge H, H values, all math is done modulo n. 
    Removing and adding characters simply involves adding or subtracting the first or last term. 
    Shifting all characters by one position to the left requires multiplying 
    the entire sum {\displaystyle H} H by a. Shifting all characters by one position to the right 
    requires dividing the entire sum  H by  a. 
    Note that in modulo arithmetic,  a can be chosen to have a multiplicative inverse a^{-1} 
    by which  H can be multiplied to get the result of the division without actually 
    performing a division.
    '''
    def __init__(self, m, w = 32):