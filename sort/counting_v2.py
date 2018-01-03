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
    _keys = [[]]*val_range
    for key in range(length):
         _keys[key].append(_array[key])
    return []

class CountingSort(SortInterface):
    def main(self):
        '''main entry point'''
        result = sort(self._data, len(self._data), max(self._data))
        if self.verbosity:
            print('------------------------------------------')
            print(result)

if __name__ == '__main__':
    CountingSort().run()