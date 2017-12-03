#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
Each node x in the binary tree has a key key(x). Nodes other than the root have a
parent p(x). Nodes may have a left child lef t(x) and/or a right child right(x).

*The invariant is*: for any node x, for all nodes y in the left subtree of x, key(y) ≤
key(x). For all nodes y in the right subtree of x key(y) ≥ key(x).
'''

import abc
import argparse
import random
import cProfile
import pstats
from os import path
from base_bst import BST

from file_operations import read_array_file, save_array_file, remove_file

import __main__

DEFAULT_LENGTH = 10

class CommonInterface(object, metaclass=abc.ABCMeta):
    '''Implements interface of performace testing of BST
    '''
    def __init__(self):
        self.context = self.get_context()
        self.verbosity = self.context.verbosity
        self._main = path.splitext(path.basename(__main__.__file__))[0]
        self.bst = None;

    def get_context(self):
        ''' Create execution context command line args
        Returns
        -------
        Object
            object with command line arguments '''
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--file", help="file name with sample data")
        parser.add_argument("-l", "--length",\
            help="length of array of sample data",\
            dest="length", type=int,\
            default=0)
        parser.add_argument('-v', '--verbosity',\
            help='increase output verbosity', action='store_true')
        return parser.parse_args()

    def _save_file(self, file_name, data):
        '''save data into file name

        :Parameters:
        filename: *String* name of the file to store data
        data: *dict* data to save'''
        return save_array_file(file_name, data, self.verbosity)

    def _read_file(self, file_name):
        ''' Reads JSON file content

        :Parameters:
        file_name: *string* - full or relative path to the file

        :Returns:
        *list* - dict of fields of json object
        '''
        return read_array_file(file_name, self.verbosity)

    @abc.abstractmethod
    def get_data(self):
        raise NotImplementedError('algorithm should be implemented')

    @abc.abstractmethod
    def main(self):
        '''Algorithm implementation '''
        raise NotImplementedError('algorithm should be implemented')

    def run(self):
        ''' run algorithm and checks results'''
        _result = '{}_results'.format(self._main)
        self.get_data()# pylint: disable=W0612
        cProfile.runctx('self.main()', globals(), locals(), _result)
        print('------------------------------------------')
        _stat = pstats.Stats(_result)
        _stat.strip_dirs().sort_stats(-1).print_stats(self._main)
        remove_file(_result)