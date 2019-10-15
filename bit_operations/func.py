# -*- coding: utf-8 -*-

def get_mask(bits):
    return (1 << bits) - 1

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)
