#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
https://courses.csail.mit.edu/6.006/spring11/exams/notes3-karatsuba
https://brilliant.org/wiki/karatsuba-algorithm/
'''
from math import ceil, floor
#math.ceil(x) Return the ceiling of x as a float, the smallest integer value greater than or equal to x.
#math.floor(x) Return the floor of x as a float, the largest integer value less than or equal to x.

def karatsuba(x, y):
    '''
    The Karatsuba algorithm decreases the number of subproblems
    to three and ends up calculating the product of two -bit numbers
    in  time--a vast improvement over the naive algorithm.
    '''
    #base case
    if x < 10 and y < 10: # in other words, if x and y are single digits
        return x*y

    n = max(len(str(x)), len(str(y)))
    #Cast n into a float because n might lie outside the representable range of integers.
    m = int(ceil(float(n)/2))

    x_H  = int(floor(x / 10**m))
    x_L = int(x % (10**m))

    y_H = int(floor(y / 10**m))
    y_L = int(y % (10**m))

    #recursive steps
    a = karatsuba(x_H,y_H)
    d = karatsuba(x_L,y_L)
    e = karatsuba(x_H + x_L, y_H + y_L) -a -d

    return int(a*(10**(m*2)) + e*(10**m) + d)

if __name__ == "__main__":
    import argparse

    PARSER = argparse.ArgumentParser('karatsuba', 'karatsuba num1 num2')
    PARSER.add_argument('num1', type=int)
    PARSER.add_argument('num2', type=int)

    OPTS = PARSER.parse_args()
    print(karatsuba(OPTS.num1, OPTS.num2))
