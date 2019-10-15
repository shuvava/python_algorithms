#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
'''
#from ...hashing import fnv

from array import array

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

def fingerprint(f, r):
    '''fingerprint f in the algorithm is partitioned into q most significant
    bits (the quotient) and r least significant bits (the remainder) using
    the quotienting technique
    '''
    divider = r#1 << r
    remainder = f // divider
    quotient = f % divider
    return quotient, remainder

class Bucket:
    '''Each bucket contains three metadata bits, all unset at the beginning:
    is_occupied, is_continuation, and is_shifted — these play
    an important role in navigating the data structure.
    '''
    def __init__(self, size=32, value=0):
        self.value = value
        self.size = size

    @property
    def is_occupied(self):
        '''is set when the bucket j is the canonical bucket
        (fq = j ) for some fingerprint f stored somewhere in the filter.
        '''
        return (self.value & (1<<(self.size-1))) > 0

    @is_occupied.setter
    def is_occupied(self, val):
        '''is set when the bucket j is the canonical bucket
        (fq = j ) for some fingerprint f stored somewhere in the filter.
        '''
        if val:
            self.value = set_bit(self.value, self.size-1)
        else:
            self.value = clear_bit(self.value, self.size-1)

    @property
    def is_continuation(self):
        '''is set when the bucket is occupied, but not by
    the first of the remainders that belong to the same bucket.
        '''
        return (self.value & (1<<(self.size-2))) > 0

    @is_continuation.setter
    def is_continuation(self, val):
        '''is set when the bucket is occupied, but not by
        the first of the remainders that belong to the same bucket.
        '''
        if val:
            self.value = set_bit(self.value, self.size-2)
        else:
            self.value = clear_bit(self.value, self.size-2)

    @property
    def is_shifted(self):
        ''' is set when the remainder in the bucket is not in its
        canonical bucket
        '''
        return (self.value & (1<<(self.size-3))) > 0

    @is_shifted.setter
    def is_shifted(self, val):
        ''' is set when the remainder in the bucket is not in its
        canonical bucket
        '''
        if val:
            self.value = set_bit(self.value, self.size-3)
        else:
            self.value = clear_bit(self.value, self.size-3)

    @property
    def val(self):
        mask = (1<<(self.size-3)) -1
        return self.value & mask

    @val.setter
    def val(self, value):
        mask = (1<<(self.size-3)) -1
        self.value = value & mask

    @property
    def isElementClusterStart(self):
        return self.is_occupied and not self.is_continuation and not self.is_shifted

    @property
    def isElementRunStart(self):
        return not self.is_continuation and (self.is_occupied or self.is_shifted)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.val == other
        if isinstance(other, self.__class__):
            return self.value == other.value
        return False

    def __gt__(self, other):
        if isinstance(other, int):
            return self.val > other
        if isinstance(other, self.__class__):
            return self.val > other.val

class QuotientFilter:
    def __init__(self, filter_size, hash_fn):
        self.num_words = filter_size
        #self.num_words = (filter_size + 31) // 32 # allign to word size
        self.entries = [None] * self.num_words # array of unsigned integers
        self.hash_fn = hash_fn

    def shift_right(self, inx, bucket):
        prev = bucket
        i = inx
        while True:
            if self.entries[i] is None:
                self.entries[i] = prev
                self.entries[i].is_continuation = 1
                self.entries[i].is_shifted = 1
                return
            else:
                curr = self.entries[i]
                self.entries[i] = prev
                prev = curr
            i = i + 1
            if i > self.num_words:
                i = 0

    def scan(self, inx):
        j = inx
        while self.entries[j].is_shifted == 1:
            j -= 1
        start = j # + 1
        while self.entries[start] and self.entries[start].is_continuation != 1:
            start += 1
        start -= 1
        end = start # + 1
        while self.entries[end] and self.entries[end].is_continuation != 1:
            end += 1
        return (start, end)

    def add(self, value):
        h = self.hash_fn(value)
        quotient, remainder = fingerprint(h, self.num_words)
        if self.entries[quotient] == None:
            b = Bucket(value=remainder)
            b.is_occupied = 1
            self.entries[quotient] = b
            return True
        self.entries[quotient].is_occupied = 1
        start, stop = self.scan(quotient)
        b = Bucket(value=remainder)
        for inx in range(start, stop):
            if self.entries[inx] == remainder:
                return True # already exist
            if self.entries[inx] > remainder:
                self.shift_right(inx, b)
                return True
        # the run should be extended with the new element
        self.shift_right(stop, b)
        return True

def test_hash(str):
    if str == 'Copenhagen':
        return 3921022591
    if str == 'Lisbon':
        return 741474681
    if str == 'Paris':
        return 4206121668
    if str == 'Stockholm':
        return 1912579905
    if str == 'Zagreb':
        return 15300639242
    if str == 'Warsaw':
        return 245338177

if __name__ == '__main__':
    b = QuotientFilter(8, hash_fn=test_hash)
    b.add('Copenhagen')
    b.add('Lisbon')
    b.add('Paris')
    b.add('Stockholm')
    b.add('Zagreb')
    b.add('567538184')
    # h = test_hash('Copenhagen')
    # quotient, remainder = fingerprint(h, 8)
    # print(f'quotient={quotient}, remainder={remainder}')
