# -*- coding: utf-8 -*-
from random import Random

mock = {
    'Copenhagen': 3711, # 3921022591,
    'Lisbon': 377, #741474681,
    'Paris':21188,#4206121668,
    'Stockholm':42817, #1912579905,
    'Zagreb':14858, #15300639242,
    'Warsaw':36929 #245338177
}

def hash_fn(val):
    if val in mock:
        return mock[val]
    hasher = Random(val).randrange
    return hasher(1_000_000)
