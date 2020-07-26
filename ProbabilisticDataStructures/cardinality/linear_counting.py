#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
the Linear Counting algorithm doesn’t store the hash values themselves,
but instead their corresponding bits, replacing the hash table with a bit
array LinearCounter of length m. It is assumed that m still is
proportional to the expected number of distinct elements n, but requires
only 1 bit per element which is feasible for most cases.
"""
from math import log
from random import Random

from .deps_import import bit_count


def get_probes(key, num_probes, filter_size):
    """
    emulate generation of hashes by `num_probes` hash functions
    * key - value to hash
    * num_probes - count of generated hashes
    * max_probe_value - max value of hash
    """
    hasher = Random(key).randrange
    for _ in range(num_probes):
        bit_index = hasher(filter_size)
        yield bit_index


def get_arr_index(probe):
    """
    calculate index in filter store(filter integer array)
    """
    return probe // 32


def get_flag(probe):
    """
    calculate flag to set/check in unsigned integer
    """
    bit_index = probe % 32
    return 1 << bit_index


class LinearCounting:
    def __init__(self, filter_size):
        num_words = (filter_size + 31) // 32 # allign to word size
        self.filter_size = num_words * 32
        self.table = [0] * num_words # array of unsigned integers
        self.hash_fn = lambda key: get_probes(key, 1, self.filter_size)

    def get_probes(self, key):
        """
        short hand for probes bit operations
        """
        for probe in self.hash_fn(key):
            array_index = get_arr_index(probe)
            mask = get_flag(probe)
            yield array_index, mask

    def add(self, key):
        for array_index, mask in self.get_probes(key):
            self.table[array_index] |= mask

    def count(self):
        """Estimating cardinality with Linear Counting
        """
        count = 0
        for item in self.table:
            count += bit_count(item)

        return -self.filter_size * log(count / self.filter_size)

    def __len__(self):
        return int(self.count())

    @staticmethod
    def create(max_elements=10000, error_rate=0.1):
        return LinearCounting(int(max_elements*error_rate*1.3))
