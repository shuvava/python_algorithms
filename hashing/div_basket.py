#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
 This module implements different ways of basketing integer values
'''

def get_basket_div_method(k, m):
    '''
        Calculate basket by k mod m

        :Parameters:
        k: *Number* - value to find basket
        m: *Number* - basket size

        :return:
         *Number* basket size
    '''
    return k % m
