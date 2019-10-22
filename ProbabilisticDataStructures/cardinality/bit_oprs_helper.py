# -*- coding: utf-8 -*-
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '../../bit_operations'))
from func import get_mask, set_bit, clear_bit, bit_count, \
    numberOfTrailingZeros, highestOneBit
