#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2017-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Non cryptographic hash function converting string into integer (hash)
https://en.wikipedia.org/wiki/MurmurHash
https://github.com/wc-duck/pymmh3/blob/master/pymmh3.py
"""
import sys as _sys

if _sys.version_info > (3, 0):
    def xrange(a, b, c):
        return range(a, b, c)


    def xencode(x):
        if isinstance(x, bytes) or isinstance(x, bytearray):
            return x
        else:
            return x.encode()
else:
    def xencode(x):
        return x
del _sys


def fmix(h):
    h ^= h >> 16
    h = (h * 0x85ebca6b) & 0xFFFFFFFF
    h ^= h >> 13
    h = (h * 0xc2b2ae35) & 0xFFFFFFFF
    h ^= h >> 16
    return h


def murmur3_hash(key: str, seed=0x0) -> int:
    """ Implements 32bit murmur3 hash. """
    key = bytearray(xencode(key))
    length = len(key)
    nblocks = int(length / 4)

    h1 = seed
    c1 = 0xcc9e2d51
    c2 = 0x1b873593
    # body
    for block_start in xrange(0, nblocks * 4, 4):
        k1 = key[block_start + 3] << 24 | \
             key[block_start + 2] << 16 | \
             key[block_start + 1] << 8 | \
             key[block_start + 0]
        k1 = (c1 * k1) & 0xFFFFFFFF
        k1 = (k1 << 15 | k1 >> 17) & 0xFFFFFFFF  # inlined ROTL32
        k1 = (c2 * k1) & 0xFFFFFFFF
        h1 ^= k1
        h1 = (h1 << 13 | h1 >> 19) & 0xFFFFFFFF  # inlined ROTL32
        h1 = (h1 * 5 + 0xe6546b64) & 0xFFFFFFFF
    # tail
    tail_index = nblocks * 4
    k1 = 0
    tail_size = length & 3

    if tail_size >= 3:
        k1 ^= key[tail_index + 2] << 16
    if tail_size >= 2:
        k1 ^= key[tail_index + 1] << 8
    if tail_size >= 1:
        k1 ^= key[tail_index + 0]

    if tail_size > 0:
        k1 = (k1 * c1) & 0xFFFFFFFF
        k1 = (k1 << 15 | k1 >> 17) & 0xFFFFFFFF  # inlined ROTL32
        k1 = (k1 * c2) & 0xFFFFFFFF
        h1 ^= k1
    # finalization
    unsigned_val = fmix(h1 ^ length)
    if unsigned_val & 0x80000000 == 0:
        return unsigned_val
    else:
        return -((unsigned_val ^ 0xFFFFFFFF) + 1)


if __name__ == "__main__":
    import sys
    import argparse

    PARSER = argparse.ArgumentParser('pymurmur3', 'pymurmur [options] "string to hash"')
    PARSER.add_argument('--seed', type=int, default=0)
    PARSER.add_argument('strings', default=[], nargs='+')
    OPTS = PARSER.parse_args()

    for str_to_hash in OPTS.strings:
        sys.stdout.write('"%s" = 0x%08X\n' % (str_to_hash, murmur3_hash(str_to_hash)))
