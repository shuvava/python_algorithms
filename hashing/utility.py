#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
from hashlib import sha1
from random import randint

def prehash(obj):
    return int(sha1(str(obj).encode('utf8')).hexdigest(), 16)

def get_odd_number(w):
    i_min = 2**(w-1)
    i_max = 2**w
    rnd = randint(i_min, i_max)
    if rnd % 2 == 0:
        return rnd
    return rnd + 1

def findLargestPrimeFactor(n):
    '''A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    By Euclid's theorem, there are an infinite number of prime numbers. Subsets of the prime numbers may be
    generated with various formulas for primes. The first 1000 primes are listed below,
    followed by lists of notable types of prime numbers in alphabetical order,
    giving their respective first terms. 1 is neither prime nor composite.
    '''
    primeFactor = 1
    i = 2

    while i <= n / i:
        if n % i == 0:
            primeFactor = i
            n /= i
        else:
            i += 1

    if primeFactor < n:
        primeFactor = n
