#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
#
"""
Given a list of bytes a, each representing one byte of
 a larger integer (ie. {0x12, 0x34, 0x56, 0x78}
 represents the integer 0x12345678), and an integer b,
 find a % b.
"""

__BASE__ = 8  # bit == 0xFF + 1


def bigint_mod(arr_bytes, mod):
    res = 0
    # Start with modding the most significant byte,
    # then repeatedly shift left.
    # This way our value never gets larger than an 2* __BASE__ bit
    for byte in arr_bytes:
        print(f'res= {res}, byte={byte}m val={(res << 8) + byte}')
        res = ((res << __BASE__) + byte) % mod
        # res = ((res * (0xFF + 1)) + byte) % mod
    return res


if __name__ == '__main__':
    val = 1005
    # val = 3432448904
    arr = list(val.to_bytes(8, byteorder='big'))
    _mod = 10
    _str = f'mod([{", ".join([f"0x{x:02X}" for x in arr])}], {_mod}) = '
    _res = bigint_mod(arr, _mod)
    print(f'{_str}{_res}')
