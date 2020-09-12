#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pathlib usage example

https://docs.python.org/3/library/pathlib.html
"""

from pathlib import Path

if __name__ == '__main__':
    print("show directories")
    p = Path('.')
    dirs = [x for x in p.iterdir() if x.is_dir()]
    for d in dirs:
        print(F'    {d}')
