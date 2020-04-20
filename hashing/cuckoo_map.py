#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Cuckoo Hashing :
Cuckoo hashing applies the idea of multiple-choice and relocation together and guarantees O(1) worst case lookup time!

Multiple-choice: We give a key two choices h1(key) and h2(key) for residing.
Relocation: It may happen that h1(key) and h2(key) are preoccupied. This is resolved by imitating the
Cuckoo bird: it pushes the other eggs or young out of the nest when it hatches.
Analogously, inserting a new key into a cuckoo hashing table may push an older key to a different location.
This leaves us with the problem of re-placing the older key.
If alternate position of older key is vacant, there is no problem.
Otherwise, older key displaces another key.
This continues until the procedure finds a vacant position, or enters a cycle.
In case of cycle, new hash functions are chosen and the whole data structure is ‘rehashed’.
Multiple rehashes might be necessary before Cuckoo succeeds.
"""

from fnv import fnv1a_32


def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


class CuckooMap:
    """
    naive implementation (store the whole key)
    """
    def __init__(self, size=12, max_displacement=4):
        if size < 2:
            raise ValueError(f'size should be mode than 2')
        self.size = size
        self.max_displacement = max_displacement
        self.__arr = [None]*self.size

    def _get_hash1(self, val):
        return fnv1a_32(int_to_bytes(val)) % self.size

    def _get_hash2(self, val):
        prime_num = 789631
        return fnv1a_32(int_to_bytes(self.size * prime_num)) % self.size

    def _add(self, hash_fn, val):
        h = hash_fn(val)
        if self.__arr[h] is None:
            self.__arr[h] = val
            return None
        return h

    def get_hash(self, inx):
        return self._get_hash1 if inx > 0 else self._get_hash2

    def add_iterative(self, val, hash_id=0, cnt=0):
        if cnt == self.max_displacement:
            return False
        hash_fn = self._get_hash1 if hash_id == 0 else self._get_hash2
        inx = self._add(hash_fn, val)
        if inx is None:
            return True
        dis = self.__arr[inx]
        result = self.add_iterative(dis, (hash_id + 1) % 2, cnt+1)
        if result:
            self.__arr[inx] = val
            return True
        return False

    def add(self, val):
        displacement = 0
        stack = []
        hash_id = 0
        while displacement < self.max_displacement:
            hash_fn = self._get_hash1 if hash_id == 0 else self._get_hash2
            inx = self._add(hash_fn, val)
            if inx is None:
                break
            stack.append((val, inx))
            val = self.__arr[inx]
            hash_id = (hash_id + 1) % 2
            displacement += 1
            if displacement == self.max_displacement:
                return False
        while displacement > 0:
            displacement -= 1
            val, inx = stack.pop()
            self.__arr[inx] = val
        return True

    def lookup(self, val):
        h = self._get_hash1(val)
        if self.__arr[h] and self.__arr[h] == val:
            return True
        h = self._get_hash2(val)
        if self.__arr[h] and self.__arr[h] == val:
            return True
        return False


if __name__ == '__main__':
    h = CuckooMap()
    for i in range(7, 20):
        h.add(i)
    print('cuckoo hashing naive example')
