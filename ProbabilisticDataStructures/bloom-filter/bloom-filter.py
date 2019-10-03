#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
the Bloom filter is represented by a bit array and can be
described by its length m and number of different hash functions {H1..Hk}
It is assumed that m is proportional to the number of expected elements
n, while k is much smaller than m.
The BloomFilter data structure is a bit array of length m where at
the beginning all bits are equal to zero, meaning the filter is empty. To
insert an element x into the filter, for every hash function hk we compute
its value j = hk (x ) on the element x and set the corresponding bit j in
the filter to one. Note, it is possible that some bits can be set multiple
times due to hash collisions.
'''
# Shamelessly borrowed (under MIT license) from http://code.activestate.com/recipes/577686-bloom-filter/
# About Bloom Filters:
#  http://en.wikipedia.org/wiki/Bloom_filter
# https://llimllib.github.io/bloomfilter-tutorial/
# https://hackernoon.com/probabilistic-data-structures-bloom-filter-5374112a7832


from math import log, ceil
from array import array
from random import Random

def get_probes(key, num_probes, filter_size):
    '''
    emulate generation of hashes by `num_probes` hash functions
    * key - value to hash
    * num_probes - count of generated hashes
    * max_probe_value - max value of hash
    '''
    hasher = Random(key).randrange
    for _ in range(num_probes):
        bit_index = hasher(filter_size)
        yield bit_index

def  countSetBits(n):
    '''unction to get no of set bits in binary
        representation of positive integer n
    '''
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

def countSetBitsOfList(arr):
    count = 0
    for item in arr:
        count += countSetBits(item)
    return count

class BloomFilterSimple():
    '''
    Naive implementation of bloom filter
    '''
    def __init__(self, filter_size, num_probes, hash_generator_fn):
        '''
        Initialize bloom filter
        * filter_size - boom filter size count of elements in bit array
        * num_probes - count of probes (count of calculated hashes for each key)
        * hash_generator_fn - function generate hashes for key
            -> hash_generator_fn(key, num_probes, filter_size)
        '''
        num_words = (filter_size + 31) // 32 # allign to word size
        self.filter_size = num_words * 32
        self.num_probes = num_probes
        self.arr = array('L', [0]) * num_words # array of unsigned integers

        self.hash_fn = lambda key: hash_generator_fn(key, self.num_probes, self.filter_size)

    @staticmethod
    def get_arr_index(probe):
        '''
        calculate index in filter store(filter integer array)
        '''
        return probe // 32

    @staticmethod
    def get_flag(probe):
        '''
        calculate flag to set/check in unsigned integer
        '''
        bit_index = probe % 32
        return 1 << bit_index

    def get_probes(self, key):
        '''
        short hand for probes bit operations
        '''
        for probe in self.hash_fn(key):
            array_index = self.get_arr_index(probe)
            mask = self.get_flag(probe)
            yield array_index, mask

    def add(self, key):
        for array_index, mask in self.get_probes(key):
            self.arr[array_index] |= mask

    def count(self):
        n = countSetBitsOfList(self.arr)
        if n < self.num_probes:
            return 0
        if n == self.num_probes:
            return 1
        if n == self.filter_size:
            return self.filter_size / self.num_probes

        return - (self.filter_size / self.num_probes) * log(1 - n/self.filter_size)

    def __contains__(self, key):
        return all(self.arr[i] & mask for i, mask in self.get_probes(key))

    def __len__(self):
        return int(self.count())

    @staticmethod
    def create(max_elements=10000, error_rate=0.1):
        '''
        calculator of settings for `BloomFilterSimple`
        * max_elements - expected count of unique elements
        * error_rate = desirable error rate
        '''
        if max_elements <= 0:
            raise ValueError('ideal_num_elements_n must be > 0')
        if not (0 < error_rate < 1):
            raise ValueError('error_rate_p must be between 0 and 1 exclusive')

        real_num_bits_m = - (max_elements * log(error_rate) / log(2) ** 2)
        num_bits = int(ceil(real_num_bits_m))

        # Verified against http://en.wikipedia.org/wiki/Bloom_filter#Probability_of_false_positives
        real_num_probes_k = (num_bits / max_elements) * log(2)
        num_probes = int(ceil(real_num_probes_k))

        return BloomFilterSimple(
            filter_size=num_bits,
            num_probes=num_probes,
            hash_generator_fn=get_probes)

if __name__ == '__main__':
    from sys import getsizeof
    states = '''Alabama Alaska Arizona Arkansas California Colorado Connecticut
        Delaware Florida Georgia Hawaii Idaho Illinois Indiana Iowa Kansas
        Kentucky Louisiana Maine Maryland Massachusetts Michigan Minnesota
        Mississippi Missouri Montana Nebraska Nevada NewHampshire NewJersey
        NewMexico NewYork NorthCarolina NorthDakota Ohio Oklahoma Oregon
        Pennsylvania RhodeIsland SouthCarolina SouthDakota Tennessee Texas Utah
        Vermont Virginia Washington WestVirginia Wisconsin Wyoming'''.split()
    bf = BloomFilterSimple.create(len(states))
    #bf = BloomFilterSimple(filter_size=1000, num_probes=14, hash_generator_fn=get_probes)
    print(f'filter_size={bf.filter_size} num_probes={bf.num_probes}')
    print(f'memory usage={getsizeof(bf.arr)}bytes; bloom filter array length={len(bf.arr)}')
    for state in states:
        bf.add(state)
    m = sum(state in bf for state in states)
    print('run assertions')
    assert m == len(states), ('m should be equal to the length of states')
    assert 'aaa' not in bf, ('should be not in bloom filter')
    print('checks successfully complied')
    l = len(bf)
    print(f'estimation of unique elements={l}, real value={len(states)}')
