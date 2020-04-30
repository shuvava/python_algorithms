#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
"""
Topological sort is implementation of linear order
 in which to put on the items(tasks and etc)
 The Graph show dependencies between different tasks
 The graph should be acyclic and directed (DAG)
Terms:
- The number of edges entering a vertex is the *vertex’s in-degree*
- DAG must have at least one vertex with in-degree 0 and at least
   one vertex with outdegree 0 (no edges leaving the vertex),
   for otherwise there would be a cycle
Complexity: O(n+m)
    where n count of vertexes; m count of edges
"""
#add parent directory with base module
import os
from sys import path

path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../common')))

from graph.graph_base import Graph


class TopologicalSort(Graph):
    """Implementation of topological sort
        relations between vertices can be presented as matrix N x N
        Since an adjacency matrix has n2 entries, it must be true that m <= n2 (from DAG definition)
        where n count of vertexes; m count of edges

    """

    def get_in_degree(self):
        """Create list of graph's nodes in-degree
            Count of vertices which depends on current one.
            Complexity: O(n+m)

        :Returns:
        *list* - list with in-degree of each node
        """
        edges = self.get_edges(True)
        _in_degree = [0] * len(edges)
        for edge_list in edges: # takes N iterations
            for edge in edge_list: # takes M iterations
                _in_degree[edge[1]] += 1
        return _in_degree

    def sort(self):
        """Make topological sort
        """
        _in_degree = self.get_in_degree()
        edges = self.get_edges(True)
        sequence = []
        _next = [inx for inx, item in enumerate(_in_degree) if item == 0]
        while _next:
            vertex = _next.pop()
            sequence.append(vertex)
            for edge in edges[vertex]:
                _in_degree[edge[1]] -= 1
                if _in_degree[edge[1]] <= 0:
                    _next.append(edge[1])
        return sequence

    def main(self):
        """main entry point"""
        indexes = self.sort()
        sequence = self.get_nodes_sequence(indexes)
        print(sequence)


if __name__ == '__main__':
    TopologicalSort().run()
