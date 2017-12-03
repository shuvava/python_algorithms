#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
Test of base_graph module
https://docs.python.org/3/library/unittest.html
'''
import unittest
import os
from sys import path

from base_graph import BaseGraph

class DumpGraph(BaseGraph):
    def main(self, _graph):
        print('main')

class TestBaseGraphMethods(unittest.TestCase):
    def setUp(self):
        self.graph = DumpGraph()
        self.graph.context.file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../graph10.json'))
        self.graph.get_graph()

    def test_read_file(self):
        file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../graph10.json'))
        graph = self.graph._read_file(file)
        self.assertIsNotNone(graph)

    def test_graph_nodes(self):
        self.assertEqual(self.graph.get_nodes_len(), 8)
    
    def test_graph_nodes_list(self):
        nodes = self.graph.get_nodes()
        self.assertEqual(len(nodes), 8)
        self.assertEqual(nodes, [7,5,3,11,8,2,9,10])
    
    def test_graph_edges(self):
        edges = self.graph.get_edges()
        self.assertIsNotNone(edges)
        self.assertEqual(edges, [[11, 8], [11], [8, 10], [2, 9], [9], [], [], []])
    
    def test_graph_edges_with_indexes(self):
        edges = self.graph.get_edges(True)
        self.assertIsNotNone(edges)
        self.assertEqual(edges, [[(11, 3), (8, 4)], [(11, 3)], [(8, 4), (10, 7)], [(2, 5), (9, 6)], [(9, 6)], [], [], []])

if __name__ == '__main__':
    unittest.main()