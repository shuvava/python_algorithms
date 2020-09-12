#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
enum example
"""
from enum import Enum, auto


class Fruit(Enum):
    APPLE = auto()
    ORANGE = auto()
    GUAVA = auto()


if __name__ == '__main__':
    print(Fruit.APPLE)
