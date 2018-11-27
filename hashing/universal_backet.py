#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
Universal hashing algorithm: 
    h(k) = [(a*k+b) mod p] mod m 
where a and b are random ∈ {0, 1, . . . p−1},
and p is a large prime (> |U|).
'''
from random import randint
from utility import findLargestPrimeFactor

class UniversalBasket:
    '''
    Calculate basket br Multiplication Method
    '''
    def __init__(self, m, w=32):
        '''
        m - count of bits of hash basket
        w - count of bit of universe (max possible value)
        '''
        if w < 4:
            raise ValueError('w should be more 4')
        self.w = w # we use 16 bit machine
        if m >= self.w:
            raise ValueError('r should be less {}'.format(self.w))
        self.m = m
        self.p = findLargestPrimeFactor(2**(self.w-1))
        self.a = randint(1, self.p)
        self.b = randint(1, self.p)

    def get_basket(self, val):
        return ((self.a * val + self.b) % self.p) % self.m
