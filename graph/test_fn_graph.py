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

class Unit_test_file_operations(unittest.TestCase):
    def setUp(self):
        self.undirected_cyclic_graph_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'graph_test.json'))

    def test_load_undirected_cyclic_graph(self):
        #act
        graph = load_graph(self.undirected_cyclic_graph_file, True)
        #assert
        self.assertIsNotNone(graph)
        self.assertTrue(graph.cyclic)
        self.assertFalse(graph.directed)
        self.assertEqual(len(graph.vertexes), 8)

if __name__ == '__main__':
    unittest.main()