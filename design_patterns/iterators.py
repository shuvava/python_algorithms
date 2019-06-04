#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Custom iterator example
taken from https://www.ics.uci.edu/~pattis/ICS-33/lectures/iterators.txt
'''

__author__ = 'Vladimir Shurygin'
__copyright__ = 'Copyright 2019, Algorithms'
__version__ = '0.0.1'
__status__ = 'dev'


class Countdown:
    def __init__(self, start):
        self.start = start  # self.start never changes; see self.n in __iter__

    # __iter__ must return an object on which __next__ can be called; it returns
    # self, which is an object of the Countdown class, which defines __next__.
    # Later we will see a problem with returning self (when the same Countdown
    # object is iterated over in a nested structure), and how to solve that
    # problem.

    def __iter__(self):
        self.n = self.start  # n attribute is added to the namespace here
        return self             # (not in __init__) and processed in __next__

    def __next__(self):
        if self.n < 0:
            raise StopIteration  # can del self.n here, after exhausting iterator
        else:
            answer = self.n  # or, without the temporary, but more confusing
            self.n -= 1  # self.n -= 1
            return answer  # return self.n+1

if __name__ == '__main__':
    cd = Countdown(10)
    for i in  cd:
        print(f'{i}, ', end='')
    print('blastoff')
