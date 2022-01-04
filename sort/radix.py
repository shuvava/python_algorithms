#!/usr/bin/env python3ß
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2017-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec07.pdf
Algorithm:
imagine each value like integer in base b
=> d = log b(k) digits
 sort (all n items) by least significant digi t-> can extract in O(1) time
 ...
 sort by most significant digit
   do sort using counting sort
   counting sort O(n+b) per digit
   => O((n+b)d) = o((n+b) log b(k))
   when b = n => o (n log n(k))
   if k <= n**c => O(n*c)
"""
from sort_interface import SortInterface


def get_offset_code(item, offset):
    ''' get internal index of char in range 0..37
    where 0 is out of range or wrong number

    :parameters:
    item *string* - to get offset
    offset *number* - offset from beggining of item

    :returns: *number* - code of char or zero if char is not from supported range
    '''
    if len(item) <= offset:
        return 0
    _chr = item[offset]
    _ascii_code = ord(_chr)
    if _ascii_code > 64 and _ascii_code < 91:  # letters
        return _ascii_code - 64 + 10
    if _ascii_code > 47 and _ascii_code < 58:  # numbers
        return _ascii_code - 47
    # unknown symbol
    return 0


def sort(_array, length, offset=0, key_len=2, val_range=37):
    '''Counting sort algorithm
    '''
    if offset >= key_len:  # max deep of sorting reached
        return _array
    _keys = [None] * (val_range + 1)
    for key in range(length):
        inx = get_offset_code(_array[key], offset)
        item = _keys[inx]
        if not item:
            _keys[inx] = [_array[key]]
        else:
            item.append(_array[key])
    result = []
    for i in range(val_range + 1):
        if _keys[i]:
            _sorted_arr = sort(_keys[i], len(_keys[i]), offset + 1, key_len)
            result.extend(_sorted_arr)
    return result


class RadixSort(SortInterface):
    def main(self):
        '''main entry point'''
        # we use [0..9,A..Z]
        result = sort(self._data, len(self._data))
        if self.verbosity:
            print('------------------------------------------')
            print(result)


if __name__ == '__main__':
    RadixSort().run()
