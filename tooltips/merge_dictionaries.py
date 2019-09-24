#!/usr/bin/env python
# -*- coding: utf-8 -*-
def merge_dictionaries(a, b):
    return {**a, **b}

if __name__ == '__main__':
    a = { 'x': 1, 'y': 2}
    b = { 'y': 3, 'z': 4}
    print(merge_dictionaries(a, b)) # {'y': 3, 'x': 1, 'z': 4}
