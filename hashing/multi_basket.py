#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#

from utility import get_odd_number

class MultiBasket:
    '''
    Calculate basket br Multiplication Method
    '''
    def __init__(self, m, w = 16):
        '''
        m - count of bits of hash basket
        w - count of bit of universe (max possible value)
        '''
        self.w = w # we use 16 bit machine
        if m >= self.w:
            raise ValueError('r should be less 16')
        self.r = m
        self.a = get_odd_number(self.w)

    def get_basket(self, val):
        return ((self.a * val) % 2 ** self.w) >> (self.w - self.r)
