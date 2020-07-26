#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://rushter.com/blog/python-memory-managment/
"""
import sys

if __name__ == '__main__':
    variable = 30
    print(sys.getsizeof(variable))  # 24
