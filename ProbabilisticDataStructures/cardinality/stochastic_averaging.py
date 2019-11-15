#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Probabilistic Counting algorithm with stochastic averaging (PCSA) Flajolet–Martin algorithm.

The solution to optimizing the Probabilistic Counting algorithm is to
apply a special procedure, called stochastic averaging, when m hash
functions are replaced by only one but its value split by quotient and
remainder, which are used to update a single counter per element.
The remainder r is used to choose one out of m counters and quotient q
to calculate the rank and find the appropriate index to be updated in
that counter.
Thus, the left-most position R of zero in the Counter after inserting
all elements from the dataset can be used as an indicator of log2 n. In
fact, a correction factor f is required and the cardinality estimation can
be done by the formula:
f = 0.77351

count_expected_elements = (1/0.77351)*(2**count_of_bits_in_counter)
'''
from math import log

from deps_import import numberOfTrailingZeros, murmur3_hash, set_bit

def get_arr_index(probe):
    '''
    calculate index in filter store(filter integer array)
    '''
    return probe // 32

def get_flag(probe):
    '''
    calculate flag to set/check in unsigned integer
    '''
    bit_index = probe % 32
    return 1 << bit_index

def rank(val):
    return numberOfTrailingZeros(val)

def left_most_zero(arr):
    num = 0
    for word in arr:
        mask = 1
        for i in range(0, 31):
            if word & mask == 0:
                return num
            num += 1
            mask = mask << 1
    return None


class StochasticAveraging:
    def __init__(self, counter_cnt, filter_size, hash_fn=None, with_small_cardinality_correction=0):
        num_words = (filter_size + 31) // 32 # allign to word size
        self.filter_size = num_words * 32
        self.num_of_counters = counter_cnt
        #self.num_bytes = num_words / 4
        self.table = []
        for _ in range(self.num_of_counters):
            self.table.append([0] * num_words)# array of unsigned integers
        self.hash_fn = hash_fn or murmur3_hash
        self.with_small_cardinality_correction = with_small_cardinality_correction

    def _set_bit(self, count_inx, probe):
        array_index = get_arr_index(probe)
        mask = get_flag(probe)
        self.table[count_inx][array_index] |= mask

    def add(self, val):
        _hash = self.hash_fn(val)
        count_inx = _hash % self.num_of_counters
        quotient = _hash // self.num_of_counters
        probe = rank(quotient)
        self._set_bit(count_inx, probe)

    def count(self):
        '''Estimating cardinality with Linear Counting
        '''
        fm_magic_constant = 0.77351
        fm_correction_constant = 0.31
        sm_correction_constant = 1.75
        count = 0
        for item in self.table:
            r = left_most_zero(item)
            count += r
        small_number_of_counters_correction = 1.0
        if self.num_of_counters < 32:
            small_number_of_counters_correction = 1 - fm_correction_constant / self.num_of_counters
        small_cardinality_correction = 0.0
        if self.with_small_cardinality_correction:
            small_cardinality_correction = 2**(- sm_correction_constant * count / self.num_of_counters)
        return (self.num_of_counters* (2**(float(count)/self.num_of_counters))- small_cardinality_correction) / (fm_magic_constant * small_number_of_counters_correction)

    def __len__(self):
        return int(self.count())

    @staticmethod
    def create(max_elements=10000, error_rate=0.1):
        count_of_counters = int((0.78/error_rate)**2)
        counter_size = int(log(max_elements/count_of_counters)+4)
        return StochasticAveraging(count_of_counters, counter_size)
