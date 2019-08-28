#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
#
# Shamelessly borrowed (under MIT license) from http://code.activestate.com/recipes/577686-bloom-filter/
# About Bloom Filters:
#  http://en.wikipedia.org/wiki/Bloom_filter
# https://llimllib.github.io/bloomfilter-tutorial/
# https://hackernoon.com/probabilistic-data-structures-bloom-filter-5374112a7832

import math
from array import array
from random import Random

def get_probes(bfilter, key):
    hasher = Random(key).randrange
    for _ in range(bfilter.num_probes):
        array_index = hasher(len(bfilter.arr))
        bit_index = hasher(32)
        yield array_index, 1 << bit_index

class BloomFilterSimple(object):
    def __init__(self, num_bits, num_probes, probe_func):
        self.num_bits= num_bits
        num_words = (num_bits + 31) // 32
        self.arr = array('L', [0]) * num_words
        self.num_probes = num_probes
        self.probe_func = get_probes

    def add(self, key):
        for i, mask in self.probe_func(self, key):
            self.arr[i] |= mask

    def match_template(self, bfilter):
        return (self.num_bits == bfilter.num_bits \
            and self.num_probes == bfilter.num_probes \
            and self.probe_func == bfilter.probe_func)

    def union(self, bfilter):
        if self.match_template(bfilter):
            self.arr = [a | b for a, b in zip(self.arr, bfilter.arr)]
        else:
            # Union b/w two unrelated bloom filter raises this
            raise ValueError("Mismatched bloom filters")

    def intersection(self, bfilter):
        if self.match_template(bfilter):
            self.arr = [a & b for a, b in zip(self.arr, bfilter.arr)]
        else:
            # Intersection b/w two unrelated bloom filter raises this
            raise ValueError("Mismatched bloom filters")

    def __contains__(self, key):
        return all(self.arr[i] & mask for i, mask in self.probe_func(self, key))


class BloomFilter(BloomFilterSimple):
    def __init__(self,
                max_elements=10000,
                error_rate=0.1,
                probe_func=get_probes):
        if max_elements <= 0:
            raise ValueError('ideal_num_elements_n must be > 0')
        if not (0 < error_rate < 1):
            raise ValueError('error_rate_p must be between 0 and 1 exclusive')
        numerator = -1 * max_elements * math.log(error_rate)
        denominator = math.log(2) ** 2
        real_num_bits_m = numerator / denominator
        num_bits = int(math.ceil(real_num_bits_m))
        # Verified against http://en.wikipedia.org/wiki/Bloom_filter#Probability_of_false_positives
        real_num_probes_k = (num_bits / max_elements) * math.log(2)
        num_probes = int(math.ceil(real_num_probes_k))
        super().__init__(num_bits, num_probes, probe_func)


if __name__ == '__main__':
    
    from random import sample
    from string import ascii_letters

    states = '''Alabama Alaska Arizona Arkansas California Colorado Connecticut
        Delaware Florida Georgia Hawaii Idaho Illinois Indiana Iowa Kansas
        Kentucky Louisiana Maine Maryland Massachusetts Michigan Minnesota
        Mississippi Missouri Montana Nebraska Nevada NewHampshire NewJersey
        NewMexico NewYork NorthCarolina NorthDakota Ohio Oklahoma Oregon
        Pennsylvania RhodeIsland SouthCarolina SouthDakota Tennessee Texas Utah
        Vermont Virginia Washington WestVirginia Wisconsin Wyoming'''.split()

    # bf = BloomFilter(max_elements=10000, error_rate=0.1)
    bf = BloomFilterSimple(num_bits=1000, num_probes=14, probe_func=get_probes)
    print(f'num_bits={bf.num_bits} num_probes={bf.num_probes}')
    for state in states:
        bf.add(state)

    m = sum(state in bf for state in states)
    print(f'{m} true positives out of {len(states)} trials')

    trials = 100000
    m = sum(''.join(sample(ascii_letters, 5)) in bf for i in range(trials))
    print(f'{trials-m} true negatives and {m} false negatives out of {trials} trials')
