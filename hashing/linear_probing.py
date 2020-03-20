#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A LinearProbing hash table can be seen as a circular array that
stores indexed values in buckets. To insert a new element x , we compute
its key k = h(x ) using a single hash function h. If the bucket that
corresponds to that key is non-empty and contains a different value,
meaning a collision, we keep looking clockwise at the next buckets until
we find a free space where we can index the element x .
"""
from random import randint

from fnv import fnv1a_32


class LinearProbing:
    '''
    naive implementation (store the whole key)
    '''

    def __init__(self, size=12):
        if size < 2:
            raise ValueError(f'size should be mode than 2')
        self.size = size
        self.__arr = [None] * self.size

    def _get_hash(self, val):
        return fnv1a_32(bytes(val)) % self.size

    def add(self, val):
        h = self._get_hash(val)
        probe = 0
        while probe < self.size:
            if self.__arr[h] is None:
                self.__arr[h] = val
                return True
            probe += 1
            h += 1
            if h >= self.size:
                h = 0
        return False

    def lookup(self, val):
        h = self._get_hash(val)
        if self.__arr[h] and self.__arr[h] == val:
            return True
        return False


if __name__ == '__main__':
    _size = 12
    arr = []
    lp = LinearProbing(size=_size)
    for _ in range(_size):
        val = randint(1, 1000)
        arr.append(val)
        result = lp.add(val)
        if not result:
            print('hash is full')
    val = randint(1, 1000)
    result = lp.lookup(val)
    assert result == False, 'Should be false'
