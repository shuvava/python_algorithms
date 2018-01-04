#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''Counting sort
Complexity: O(n);
'''
from sort_interface import SortInterface 

def sort(_array, length, val_range):
    _keys = [None]*(val_range+1)
    for key in range(length):
        item = _keys[_array[key]]
        if not item:
             _keys[_array[key]] = [_array[key]]
        else:
            item.append(_array[key])
    result = []
    for i in range(val_range+1):
        if _keys[i]:
            result.extend(_keys[i])
    return result

class CountingSort(SortInterface):
    def main(self):
        '''main entry point'''
        result = sort(self._data, len(self._data), max(self._data))
        if self.verbosity:
            print('------------------------------------------')
            print(result)

if __name__ == '__main__':
    CountingSort().run()