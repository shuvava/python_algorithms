#!/usr/bin/env python
# -*- coding: utf-8 -*-


def all_unique(lst):
    return len(lst) == len(set(lst))


if __name__ == '__main__':
    x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
    y = [1, 2, 3, 4, 5]
    print(all_unique(x))  # False
    print(all_unique(y))  # True
