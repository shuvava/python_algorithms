#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implementation of Fowler/Noll/Vo hash algorithm in pure Python.

The FNV algorithm maintains an internal state that is initialized
to a special offset basis. After that, it iterates over the input blocks
of 8 bits and performs the multiplication of the state on some large
numerical constant, called the FNV Prime, followed by applying logical
exclusive OR (XOR) to the input block.

links:
https://github.com/znerol/py-fnvhash/blob/master/fnvhash/__init__.py
http://isthe.com/chongo/tech/comp/fnv/
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import sys

FNV_32_PRIME = 0x01000193  # 16,777,619‬
FNV_64_PRIME = 0x100000001b3

FNV0_32_INIT = 0
FNV0_64_INIT = 0
FNV1_32_INIT = 0x811c9dc5  # 2,166,136,261
FNV1_32A_INIT = FNV1_32_INIT
FNV1_64_INIT = 0xcbf29ce484222325
FNV1_64A_INIT = FNV1_64_INIT

if sys.version_info[0] == 3:
    _get_byte = lambda c: c
else:
    _get_byte = ord


def fnv(data, hval_init, fnv_prime, fnv_size):
    """
    Core FNV hash algorithm used in FNV0 and FNV1.
    """
    assert isinstance(data, bytes)

    hval = hval_init
    for byte in data:
        hval = (hval * fnv_prime) % fnv_size
        hval = hval ^ _get_byte(byte)
    return hval


def fnva(data, hval_init, fnv_prime, fnv_size):
    """
    Alternative FNV hash algorithm used in FNV-1a.
    """
    assert isinstance(data, bytes)

    hval = hval_init
    for byte in data:
        hval = hval ^ _get_byte(byte)
        hval = (hval * fnv_prime) % fnv_size
    return hval


def fnv0_32(data, hval_init=FNV0_32_INIT):
    """
    Returns the 32 bit FNV-0 hash value for the given data.
    """
    return fnv(data, hval_init, FNV_32_PRIME, 2 ** 32)


def fnv1_32(data, hval_init=FNV1_32_INIT):
    """
    Returns the 32 bit FNV-1 hash value for the given data.
    """
    return fnv(data, hval_init, FNV_32_PRIME, 2 ** 32)


def fnv1a_32(data, hval_init=FNV1_32_INIT):
    """
    Returns the 32 bit FNV-1a hash value for the given data.
    """
    return fnva(data, hval_init, FNV_32_PRIME, 2 ** 32)


def fnv0_64(data, hval_init=FNV0_64_INIT):
    """
    Returns the 64 bit FNV-0 hash value for the given data.
    """
    return fnv(data, hval_init, FNV_64_PRIME, 2 ** 64)


def fnv1_64(data, hval_init=FNV1_64_INIT):
    """
    Returns the 64 bit FNV-1 hash value for the given data.
    """
    return fnv(data, hval_init, FNV_64_PRIME, 2 ** 64)


def fnv1a_64(data, hval_init=FNV1_64_INIT):
    """
    Returns the 64 bit FNV-1a hash value for the given data.
    """
    return fnva(data, hval_init, FNV_64_PRIME, 2 ** 64)


if __name__ == "__main__":
    val = fnv1a_32(b'foo')
    _hash = hex(val)
    print(f'hex={_hash} val={val}')
