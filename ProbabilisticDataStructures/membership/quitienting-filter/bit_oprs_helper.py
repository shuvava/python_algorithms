# -*- coding: utf-8 -*-
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '../../../bit_operations'))
from func import get_mask, set_bit, clear_bit, bit_count, \
    numberOfTrailingZeros, highestOneBit

def is_occupied(val):
    return (val & 1) > 0

def is_occupied_set(val):
    return set_bit(val, 0)

def is_occupied_clear(val):
    return clear_bit(val, 0)

def is_continuation(val):
    return (val & 2) > 0

def is_continuation_set(val):
    return set_bit(val, 1)

def is_continuation_clear(val):
    return clear_bit(val, 1)

def is_shifted(val):
    return (val & 4) > 0

def is_shifted_set(val):
    return set_bit(val, 2)

def is_shifted_clear(val):
    return clear_bit(val, 2)

def isElementClusterStart(val):
    return is_occupied(val) and not is_continuation(val) and not is_shifted(val)

def isElementRunStart(val):
    return not is_continuation(val) and (is_occupied(val) or is_shifted(val))

def is_empty(val):
    return (val & 7) == 0

def get_remainder(elt):
    return elt >> 3

def set_reminder(val):
    return val << 3

def get_table_size(quotient_bits, remainder_bits):
    bits = (1<<quotient_bits)*(remainder_bits+3)
    return (bits + 63) // 64
