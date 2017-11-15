#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
base functionality of graph
 - read from file
 - write to file
 - generate
'''
import abc
import argparse
import cProfile
import pstats
from os import path
import json
import __main__

DEFAULT_LENGTH = 10

class BaseGraph(object, metaclass=abc.ABCMeta):
    '''Implementation of base functionality
    '''
    def get_context(self):
        ''' Create execution context command line args
        '''
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--file", help="file name with sample data")
        parser.add_argument('-v', '--verbosity',\
            help='increase output verbosity', action='store_true')
        return parser.parse_args()

    def __init__(self):
        self.context = self.get_context()
        self.verbosity = self.context.verbosity
        self._main = path.splitext(path.basename(__main__.__file__))[0]
        self.graph = None

    def _save_file(self, file_name, data):
        '''save data into file name

        :Parameters:
        filename: *String* name of the file to store data
        data: *list* data to save'''
        raise NotImplementedError('algorithm should be implemented')

    def _nodes(self):
        return self.graph['nodes']
    
    def get_nodes_len(self):
        return len(self._nodes())

    def get_nodes(self):
        '''return list of nodes with node's id
        '''
        if (self._nodes_arr):
            return self._nodes_arr
        nodes = self._nodes()
        self._nodes_arr = []
        for node in nodes:
            self._nodes_arr.append(node['id'])
        return self._nodes_arr

    def _get_node_index(self, id):
        '''return index of node with Id = id
        '''
        nodes = self.get_nodes()
        for inx, node in enumerate(nodes):
            if node == id:
                return inx
        return None

    def get_edges(self, with_index = False):
        '''returns list of edges for node id
        '''
        edges = self.graph['edges']
        nodes = self.get_nodes()
        data = [edge['targets'] for node in nodes for edge in edges if edge['source']==node]
        if with_index:
            return [[(i, self._get_node_index(i)) for i in items] for items in data]
        return data


    def _read_file(self, file_name):
        ''' Reads JSON file content

        :Parameters:
        file_name: *string* - full or relative path to the file

        :Returns:
        *list* - List of fields
        '''
        if not path.exists(file_name):
            return []
        if self.verbosity:
            print('reading file {}'.format(file_name))
        try:
            with open(file_name, 'r') as file:
                return json.load(file)
        except PermissionError:
            print('unable to read the file')

    def get_graph(self):
        '''Generate or load from file graph
        '''
        _filename = ''
        self.graph = None
        self._nodes_arr = None
        if self.context.file is None:
            return
        _filename = self.context.file.strip()
        self.graph  = self._read_file(_filename)['graph']
        if self.verbosity:
            print(self.graph)

    @abc.abstractmethod
    def main(self, _graph):
        '''Algorithm implementation '''
        raise NotImplementedError('algorithm should be implemented')

    def run(self):
        ''' run algorithm and checks results'''
        _result = '{}_results'.format(self._main)
        self.get_graph()# pylint: disable=W0612
        cProfile.runctx('self.main()', globals(), locals(), _result)
        print('------------------------------------------')
        _stat = pstats.Stats(_result)
        _stat.strip_dirs().sort_stats(-1).print_stats(self._main)
