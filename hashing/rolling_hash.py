#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
"""
Implementation of Rolling hash function
https://en.wikipedia.org/wiki/Rolling_hash
https://www.geeksforgeeks.org/searching-for-patterns-set-3-rabin-karp-algorithm/
https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
"""
from hashing.utility import findLargestPrimeFactor


class PolynomialRollingHash:
    """
    Polynomial rolling hash
    H = C1*a^(k-1)+C2*a^(k-2)+...Ck*a^(0)

    where
        C1..Ck - ASII code of string
        k      - max length of string

    In order to avoid manipulating huge H, H values, all math is done modulo n.
    Removing and adding characters simply involves adding or subtracting the first or last term.
    Shifting all characters by one position to the left requires multiplying
    the entire sum H by a. Shifting all characters by one position to the right
    requires dividing the entire sum H by  a.
    Note that in modulo arithmetic, a can be chosen to have a multiplicative inverse a^{-1}
    by which  H can be multiplied to get the result of the division without actually
    performing a division.
    """

    def __init__(self, base=256):
        """
        base = max number
        """
        if base < 256:
            base = 256
        self.arr = []
        self.hash = 0
        self.base = base
        self.prime = findLargestPrimeFactor(base)
        self.magic = 1
        self.mod_adjustment = self.base * self.prime

    def add_symbol(self, c):
        self.add(ord(c))

    def shift_symbol(self, c):
        self.shift(ord(c))

    def add(self, i):
        self.hash = (self.base * self.hash + i) % self.prime
        self.arr.append(i)
        self._upd_magic()

    def _upd_magic(self):
        h = len(self.arr) - 1
        if h <= 0:
            self.magic = 1
        else:
            self.magic = self.base ** h % self.prime

    def remove(self, update_magic=True):
        self.hash = (self.hash - self.arr[0] * self.magic % self.prime) % self.prime
        self.arr.pop(0)
        if update_magic:
            self._upd_magic()

    def shift(self, i):
        self.hash = ((self.hash - self.arr[0] * self.magic % self.prime) * self.base + i) % self.prime
        self.arr.pop(0)
        self.arr.append(i)
