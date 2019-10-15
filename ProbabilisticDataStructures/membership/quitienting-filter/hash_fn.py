#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '../../../hashing'))

from fnv import fnv1a_32 as hash_fn

if __name__ == '__main__':
    val = hash_fn(b'foo')
    _hash = hex(val)
    print(f'hex={_hash} val={val}')
