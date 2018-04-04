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

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def findLargestPrimeFactor(n):
    '''A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    By Euclid's theorem, there are an infinite number of prime numbers. Subsets of the prime numbers may be
    generated with various formulas for primes. The first 1000 primes are listed below,
    followed by lists of notable types of prime numbers in alphabetical order,
    giving their respective first terms. 1 is neither prime nor composite.
    '''
    while n > 2 and not isPrime(n):
        n -= 1
    return n

def findLargestPrimeFactor_old(n):

    prime_factor = 1
    i = 2
    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1
    if prime_factor < n:
        prime_factor = n
    return int(prime_factor)
