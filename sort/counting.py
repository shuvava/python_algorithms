#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''Counting sort
Complexity: O(n);
'''
#add parent directory with base module
import os
from sys import path

path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../common')))

from base_interface import BaseAlg # pylint: disable=C0413

class CountingSort(BaseAlg):
    ''' Implementation of Counting Sort
    Thomas H. Cormen Algorithms Unlocked (2013) page 67
    '''

    @staticmethod
    def count_keys_equal_or_less(_array, length, val_range):
        '''computing how many elements have sort
        keys equal or less to that value

        :parameters:
        _array: *list* - array of elements
        length: *Number* - length of sorting array
        valRange: *Number* - max value in sorting array

        :returns: *list* - An array equal_or_less[0..valRange-1] such that equal_or_less[j]
        contains the number of elements of A that equal or less j ,
        for j = 0,1,2...,valRange-1.
        '''
        _keys = [0] * val_range
        # COUNT-KEYS-EQUAL
        for inx in range(0, length):
            key = _array[inx]-1
            _keys[key] = _keys[key] + 1
        # COUNT-KEYS-LESS
        # equal = _keys[0]
        less = 0
        for inx in range(0, val_range):
            # _keys[inx], equal = equal, _keys[inx]
            _keys[inx] = less + _keys[inx]
            less = _keys[inx]
        return _keys

    @staticmethod
    def rearrange(_array, _keys, length):
        '''rearrange elements in original array

        :parameters:
        _array: *list* - array of elements
        _keys: *list* - array of keys equal or less
        length: *Number* - length of sorting array

        :returns: *list* - An array of sorted elements
        '''
        result = [0] * length
        for inx in range(0, length):
            key = _array[inx]
            _inx = _keys[key-1]-1
            result[_inx] = _array[inx]
            _keys[key-1] = _keys[key-1] - 1
        return result

    def main(self, _array):
        '''main entry point'''
        keys = self.count_keys_equal_or_less(_array, len(_array), max(_array))
        result = self.rearrange(_array, keys, len(_array))
        if self.verbosity:
            print('------------------------------------------')
            print(result)

if __name__ == '__main__':
    CountingSort().run()
