#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom iterator example
taken from https://www.ics.uci.edu/~pattis/ICS-33/lectures/decoratorspackages.txt
"""

__author__ = 'Vladimir Shurygin'
__copyright__ = 'Copyright 2019, Algorithms'
__version__ = '0.0.1'
__status__ = 'dev'


class Memoize:
    def __init__(self,f):
        self._f = f
        self._cache = {}

    def __call__(self,*args):
        if args in self._cache:
            return self._cache[args]
        else:
            answer = self._f(*args)        # Recursive calls will set cache too
            self._cache[args] = answer
        return answer

    def reset_cache(self):
        self._cache = {}


def memoize1(f):
    def wrapper(*args):
        if args in wrapper._cache:
            return wrapper._cache[args]
        else:
            answer = f(*args)
            wrapper._cache[args] = answer
            return answer

    wrapper._cache = {}

    def reset_cache():
        wrapper._cache = {}
    wrapper.reset_cache = reset_cache

    return wrapper


def memoize2(f):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            answer = f(*args)
            cache[args] = answer
            return answer

    def reset_cache():
        cache.clear()

    def reset_cache2():
        nonlocal cache # Allows cache in enclosing scope to be updated
        cache = {}
    wrapper.reset_cache = reset_cache
    wrapper.reset_cache2 = reset_cache2

    return wrapper


@Memoize
def fib(n):
    if n == 0:
        return 1
    if  n == 1:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    res = fib(5)
    print(f'{res} cache={fib._cache}')
