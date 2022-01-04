#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2017-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from datetime import datetime

import pandas as pd
from datasketch import HyperLogLogPlusPlus

_cln_end_date = 'EndDate'
_cln_host_id = 'hostId'
_cln_value = 'val'
_cln_hll = 'hll'
# test input data set 
inp = []
inp.append({_cln_end_date: datetime.strptime('01/20/2005', '%m/%d/%Y'), _cln_host_id: 1, _cln_value: 1})
inp.append({_cln_end_date: datetime.strptime('01/21/2005', '%m/%d/%Y'), _cln_host_id: 1, _cln_value: 1})
inp.append({_cln_end_date: datetime.strptime('01/20/2005', '%m/%d/%Y'), _cln_host_id: 1, _cln_value: 2})
InputDataSet = pd.DataFrame(inp)

# calc hll
hll_dict = {}
for index, row in InputDataSet.iterrows():
    key = '{}_{}'.format(row[_cln_end_date].strftime("%d/%m/%Y"), row[_cln_host_id])
    print(key)
    if key in hll_dict:
        print('in')
        hll = hll_dict[key][_cln_hll]
    else:
        print('not')
        hll = HyperLogLogPlusPlus(p=12)  # max p=16
        # if row[_cln_hll]: # init from exist hash
        #     _arr= np.fromstring(digest, dtype=int, sep=" ")
        #     hll = HyperLogLogPlusPlus(reg= _arr)
        hll_dict[key] = {_cln_hll: hll, _cln_end_date: row[_cln_end_date], _cln_host_id: row[_cln_host_id]}
    hll.update(str(row[_cln_value]).encode('utf8'))

out = []
# prepare output
for key, value in hll_dict.items():
    hll = value[_cln_hll]
    buf = bytearray(hll.bytesize())
    hll.serialize(buf)
    print(hll.bytesize())
    obj = {_cln_hll: bytes(buf), _cln_end_date: value[_cln_end_date], _cln_host_id: value[_cln_host_id]}
    out.append(obj)
    print('key:{}; estimation:{}'.format(key, hll.count()))

OutputDataSet = pd.DataFrame(out)
# test output
for index, row in OutputDataSet.iterrows():
    print("index={}; {}:{};".format(index, _cln_end_date, row[_cln_end_date]))
# hll = HyperLogLogPlusPlus(p=12) # max p=16
# if digest and len(digest)> 0:
# 	_arr= np.fromstring(digest, dtype=int, sep=" ")
# 	hll = HyperLogLogPlusPlus(reg= _arr) 

# for i in InputDataSet["id"]:
# 	hll.update(str(i).encode(''utf8''))
# #print(hll.count())
# estimation = int(hll.count())
# __digest = hll.digest([])
# #print(__digest)
# _digest = " ".join(map(str, __digest))
# digest = _digest
# #print(digest)
