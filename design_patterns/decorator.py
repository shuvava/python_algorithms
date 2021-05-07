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


class TrackCalls:
    def __init__(self, f):
        self._f = f
        self._calls = 0

    def __call__(self, *args, **kargs):  # bundle arbitrary arguments to this call
        self._calls += 1
        return self._f(*args, **kargs)  # unbounded arbitrary arguments to call f

    def called(self):
        return self._calls

    def reset(self):
        self._calls = 0


def track_calls(f):
    """
    In fact, we can define the track_calls function below, so that we can call the
    methods called/reset on it. Here we bind the attributes reset/called to
    functions (on named - because it executes a statement - and one lambda, because
    it just returns a value)
    """

    def call(*args, **kargs):
        call._calls += 1
        return f(*args, **kargs)

    call._calls = 0  # define calls, reset, and called attributes on

    # call function-object; bind the first to a
    def reset(): call._calls = 0  # data object, the next two to function objects

    call._reset = reset

    call.called = lambda: call._calls

    return call


@TrackCalls
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# which is equivalent to
def factorial_test(n):
    if n == 0:
        return 1
    else:
        return n * factorial_test(n - 1)


factorial_test = TrackCalls(factorial_test)

if __name__ == '__main__':
    res = factorial(3)
    print(f'func result {res}; count of calls = {factorial.called()}')
    factorial.reset()
    res2 = factorial_test(3)
    print(f'func result {res2}; count of calls = {factorial_test.called()}')
    factorial_test.reset()
