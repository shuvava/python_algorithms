#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
Test of base_bst module
https://docs.python.org/3/library/unittest.html
'''
import unittest
import os

from undirected_cyclic import Graph
from vertex import Vertex
from fn_graph import load_graph
from breath_first import bfs_undirected_cyclic
from deapth_first import dfs_undirected_cyclic

class Unit_test_file_operations(unittest.TestCase):
    def setUp(self):
        self.undirected_cyclic_graph_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'graph_test.json'))

    def test_load_undirected_cyclic_graph(self):
        #act
        graph = load_graph(self.undirected_cyclic_graph_file, True)
        vertex = graph.get_vertex(0)
        #assert
        self.assertIsNotNone(graph)
        self.assertTrue(graph.cyclic)
        self.assertFalse(graph.directed)
        self.assertEqual(len(graph.vertexes), 8)
        self.assertEqual(len(vertex.adj), 2)

    def test_bfs_undirected_cyclic(self):
        #arrange
        graph = load_graph(self.undirected_cyclic_graph_file, False)
        #act
        bfs = bfs_undirected_cyclic(graph, 0)
        #assert
        self.assertIsNotNone(bfs)
        self.assertIsNotNone(bfs[0])
        self.assertIsNotNone(bfs[1])

    def test_dfs_undirected_cyclic(self):
        #arrange
        graph = load_graph(self.undirected_cyclic_graph_file, False)
        #act
        dfs = dfs_undirected_cyclic(graph,0)
        #assert
        self.assertIsNotNone(dfs)
        self.assertIsNotNone(dfs[0])
        self.assertIsNotNone(dfs[1])

if __name__ == '__main__':
    unittest.main()