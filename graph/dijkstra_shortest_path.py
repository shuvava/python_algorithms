
#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
Dijkstra algorithm find shortest path in graph Shortest paths in graphs without negative edges.
'''
#add parent directory with base module
import os
from sys import path
path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bst')))

from undirected_cyclic import Graph
from vertex import Vertex
from bst_heap_min import MinHeap

def dijkstra_min_priority_queue(graph, start, finish):
    ''' Implementation with min-priority queue
    BigO = V**2, (where |V| is the number of nodes).
    '''
    if not isinstance(graph, Graph):
        return None
    if start is None:
        return None
    heap = MinHeap()
    visited = {}
    heap.push({'vertex':start.id, 'value':0})
    path = {}
    while heap.array:
        obj = heap.pop()
        vertex = graph.get_vertex(obj['vertex'])
        if vertex.id in visited:
            continue
        for adj_vertex_id in vertex.adj:
            adj_vertex = vertex.adj[adj_vertex_id]
            edge_property = vertex.get_edge_property(adj_vertex_id)
            heap.push({'vertex':adj_vertex, 'value':None})

    pass
