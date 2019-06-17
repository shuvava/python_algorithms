#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
#
'''
Given two integers, write a function to sum the numbers
without using any arithmetic operators.
'''

def custom_sum(val1, val2):
    result = 0
    val = 1
    max_val = max(val1, val2)
    while val <= max_val:
        bit1 = val1 & val
        bit2 = val2 & val
        if (bit1 & bit2) > 0:
            if (result & val << 1) == 1:
                result |= val << 2
            else:
                result |= val << 1
        else:
            result |= bit1 | bit2
        val = val << 1
    return result

def custom_sum2(val1, val2):
    if val2 == 0:
        return val1
    partial_sum = val1 ^ val2 # xor
    _next = (val1 & val2) << 1
    return custom_sum2(partial_sum, _next)

if __name__ == '__main__':
    _val1 = 5
    _val2 = 10
    _result = custom_sum2(_val1, _val2)
    print(f'custom_sum({_val1}, {_val2}) == {_result}')
