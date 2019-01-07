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
from breath_first import bfs_undirected_cyclic, get_shortest_path
from deapth_first import dfs_undirected_cyclic, dfs_undirected_cyclic_b, dfs_detect_cycle

class Unit_test_file_operations(unittest.TestCase):
    def setUp(self):
        self.undirected_cyclic_graph_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'graph_test.json'))
        self.directed_cyclic_graph_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'graph_test_dfs.json'))

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

    def test_load_directed_cyclic_graph(self):
        #act
        graph = load_graph(self.directed_cyclic_graph_file, True)
        vertex = graph.get_vertex(0)
        #assert
        self.assertIsNotNone(graph)
        self.assertTrue(graph.cyclic)
        self.assertFalse(graph.directed)
        self.assertEqual(len(graph.vertexes), 6)
        self.assertEqual(len(vertex.adj), 2)

    def test_bfs_undirected_cyclic(self):
        #arrange
        graph = load_graph(self.undirected_cyclic_graph_file, False)
        #act
        bfs = bfs_undirected_cyclic(graph, 0)
        #assert
        self.assertIsNotNone(bfs)
        self.assertIsNotNone(bfs[0])
        self.assertEqual(len(bfs[0]), 8)
        self.assertEqual(bfs[0][graph.get_vertex('7')], 3)
        self.assertIsNotNone(bfs[1])
        self.assertEqual(bfs[1][graph.get_vertex('4')], graph.get_vertex('3'))

    def test_get_shortest_path(self):
        #arrange
        graph = load_graph(self.undirected_cyclic_graph_file, False)
        #act
        path = get_shortest_path(graph, 0, 6)
        #assert
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 4)
        self.assertEqual(path[2], graph.get_vertex('3'))


    def test_dfs_directed_cyclic(self):
        #arrange
        graph = load_graph(self.directed_cyclic_graph_file, False)
        #act
        dfs = dfs_undirected_cyclic_b(graph, 1)
        #dfs = bfs_undirected_cyclic(graph, 1)

        #assert
        levels = dfs[0]
        relations = dfs[1]
        self.assertIsNotNone(dfs)
        self.assertIsNotNone(levels)
        self.assertEqual(len(levels), 4)
        self.assertTrue(graph.get_vertex(0) not in levels)
        self.assertIsNotNone(relations)
        self.assertEqual(len(relations), 4)
        self.assertTrue(graph.get_vertex(0) not in relations)

    def test_detect_cycle(self):
        #arrange
        graph = load_graph(self.directed_cyclic_graph_file, False)
        #act
        result1 = dfs_detect_cycle(graph, 1)
        result2 = dfs_detect_cycle(graph, 5)
        #assert
        self.assertTrue(result1)
        self.assertFalse(result2)
  

if __name__ == '__main__':
    unittest.main()