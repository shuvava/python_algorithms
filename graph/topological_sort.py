#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
Topological sort is implementation of linear order
 in which to put on the items(tasks and etc)
 The Graph show dependencies between different tasks
 The graph should be acyclic and directed (DAG)
Terms:
- The number of edges entering a vertex is the *vertex’s in-degree*
- DAG must have at least one vertex with in-degree 0 and at least
   one vertex with outdegree 0 (no edges leaving the vertex),
   for otherwise there would be a cycle
'''
#add parent directory with base module
import os
from sys import path

path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../common')))

from base_graph import BaseGraph

class TopologicalSort(BaseGraph):
    '''Implementation of topological sort
    '''

    def get_in_degree(self):
        '''Create list of graph's nodes in-degree

        :Returns:
        *list* - list with in-degree of each node
        '''
        edges = self.get_edges(True)
        _in_degree = [0] * len(edges)
        for edge_list in edges:
            for edge in edge_list:
                _in_degree[edge[1]] += 1
        return _in_degree

    def sort(self):
        '''Make topological sort
        '''
        _in_degree = self.get_in_degree()
        edges = self.get_edges(True)
        result = []
        next = [inx for inx, item in enumerate(_in_degree) if item == 0]
        while not next:
             

    def main(self):
        '''main entry point'''
        in_degree = self.get_in_degree()
        print(in_degree)

if __name__ == '__main__':
    TopologicalSort().run()
