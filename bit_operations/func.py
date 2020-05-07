# -*- coding: utf-8 -*-


def get_mask(bits):
    return (1 << bits) - 1


def set_bit(value, bit):
    return value | (1<<bit)


def clear_bit(value, bit):
    return value & ~(1<<bit)


def bit_count(x):
    x = ((x >> 1) & 0b01010101010101010101010101010101) \
       + (x       & 0b01010101010101010101010101010101)
    x = ((x >> 2) & 0b00110011001100110011001100110011) \
       + (x       & 0b00110011001100110011001100110011)
    x = ((x >> 4) & 0b00001111000011110000111100001111) \
       + (x       & 0b00001111000011110000111100001111)
    x = ((x >> 8) & 0b00000000111111110000000011111111) \
       + (x       & 0b00000000111111110000000011111111)
    x = ((x >> 16)& 0b00000000000000001111111111111111) \
       + (x       & 0b00000000000000001111111111111111)
    return x


def numberOfTrailingZeros(i):
    """Returns the number of zero bits following the lowest-order ("rightmost")
    one-bit in the two's complement binary representation of the specified
    value.  Returns 64 if the specified value has no
    one-bits in its two's complement representation, in other words if it is
    equal to zero.
    """
    mask32 = 0b11111111111111111111111111111111
    if i == 0: return 64
    n = 63
    y = i & mask32
    if y != 0:
        n = n -32
        x = y
    else:
        x = i >> 32
    y = (x << 16) & mask32
    if y != 0:
        n = n -16
        x = y
    y = (x << 8) & mask32
    if y != 0:
        n = n - 8
        x = y
    y = (x << 4) & mask32
    if y != 0:
        n = n - 4
        x = y
    y = (x << 2) & mask32
    if y != 0:
        n = n - 2
        x = y
    return n - (((x << 1)& mask32) >> 31)


def highestOneBit(i):
    """Returns a value with at most a single one-bit, in the
      position of the highest-order ("leftmost") one-bit in the specified
      value.  Returns zero if the specified value has no
      one-bits in its two's complement binary representation, that is, if it
      is equal to zero.
    """
    i |= (i >>  1)
    i |= (i >>  2)
    i |= (i >>  4)
    i |= (i >>  8)
    i |= (i >> 16)
    i |= (i >> 32)
    return i - (i >> 1)
