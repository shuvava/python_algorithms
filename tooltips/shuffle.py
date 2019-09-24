#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import shuffle

if __name__ == '__main__':
    foo = [1, 2, 3, 4]
    shuffle(foo)
    print(foo) # [1, 4, 3, 2] , foo = [1, 2, 3, 4]
