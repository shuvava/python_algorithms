#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
import abc
import random
#add parent directory with base module
import os
from sys import path

path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../common')))
from common_interface import CommonInterface

DEFAULT_LENGTH = 10

def gen_array(length, max_value=1000):
    '''Generates random array
    Parameters
    ----------
    length: int
        the length of random array
    Returns
    -------
        list of random elements
    '''
    _data = []
    _i = 0
    while _i < length:
        _data.append(random.randrange(1, max_value))
        _i += 1
    return _data

class SortInterface(CommonInterface, metaclass=abc.ABCMeta):
    def get_data(self):
        _filename = ''
        if self.context.file is not None:
            _filename = self.context.file.strip()
        if self.context.length > 0:
            _data = gen_array(self.context.length, 10 * self.context.length)
            if _filename:
                self._save_file(_filename, _data)
        else:
            if not _filename:
                _data = gen_array(DEFAULT_LENGTH, 10 * DEFAULT_LENGTH)
            else:
                _data = self._read_file(_filename)[0]
        if self.verbosity:
            print(_data)
        self._data = _data
        return _data

    @abc.abstractmethod
    def main(self):
        '''Algorithm implementation '''
        raise NotImplementedError('algorithm should be implemented')