#!/usr/bin/env python
# -*- coding: utf-8 -*-
def palindrome(a):
    return a == a[::-1]

if __name__ == '__main__':
    print(palindrome('mom')) # True
