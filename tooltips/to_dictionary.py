#!/usr/bin/env python
# -*- coding: utf-8 -*-


def to_dictionary(keys, values):
    return dict(zip(keys, values))


if __name__ == '__main__':
    keys = ["a", "b", "c"]
    values = [2, 3, 4]
    print(to_dictionary(keys, values)) # {'a': 2, 'c': 4, 'b': 3}
