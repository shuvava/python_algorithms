#!/usr/bin/env python3
# encoding: utf-8
'''
See more https://docs.python.org/3.2/library/itertools.html#itertools.combinations
'''
from itertools import *

def permutation(s):
    for item in permutations(s):
        if item:
            print(''.join(i for i in item), end=' ') # abc acb bac bca cab cba
    print('')

def permutation2(s, i):
    for item in permutations(s, i):
        if item:
            print(''.join(i for i in item), end=' ') # abc acb bac bca cab cba
    print('')

def permutation3(s, i):
    for item in product(s, repeat=i):
        if item:
            print(''.join(i for i in item), end=' ') # abc acb bac bca cab cba
    print('')

def combination(s, i):
    for item in combinations(s, i):
        if item:
            print(''.join(i for i in item), end=' ') # abc acb bac bca cab cba
    print('')

def combination2(s, i):
    for item in combinations_with_replacement(s, i):
        if item:
            print(''.join(i for i in item), end=' ') # abc acb bac bca cab cba
    print('')

if __name__ == '__main__':
    permutation('abc')
    permutation('abb')
    permutation2('abc', 2)
    permutation3('abc', 2)
    combination('abcd', 2)
    combination2('abcd', 2)
