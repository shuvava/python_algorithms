#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter


def anagram(first, second):
    return Counter(first) == Counter(second)


if __name__ == '__main__':
    print(anagram("abcd3", "3acdb"))
