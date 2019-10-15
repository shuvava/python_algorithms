# -*- coding: utf-8 -*-
from random import Random

mock = {
    'Copenhagen':3921022591,
    'Lisbon': 741474681,
    'Paris':4206121668,
    'Stockholm':1912579905,
    'Zagreb':15300639242,
    'Warsaw':245338177
}

def hash_fn(val):
    if val in mock:
        return mock[val]
    hasher = Random(val).randrange
    return hasher(1_000_000)
