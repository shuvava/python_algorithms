#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
"""
it is test of external library
for import hyperloglog
    https://github.com/svpcom/hyperloglog
for from datasketch import HyperLogLogPlusPlus
    https://github.com/ekzhu/datasketch
"""
#import hyperloglog
from datasketch import HyperLogLogPlusPlus
import os
from sys import path

path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../common')))
from file_operations import read_array_file

if __name__ == '__main__':
    arr = read_array_file('./hyperloglog/data.txt', True)
    #hll = hyperloglog.HyperLogLog(0.01)  # accept 1% counting error
    hll = HyperLogLogPlusPlus()
    cnt = len(arr)
    print('count = {}; distinct = {}'.format(cnt, 2103130))
    for i in arr:
        hll.update(str(i).encode('utf8'))
        #hll.add(str(i))
    print(hll.count())
    print(hll.digest([]))
    #print(len(hll))
