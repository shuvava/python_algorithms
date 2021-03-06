# -*- coding: utf-8 -*-
"""
implementation of Breath-First algorithm
Breadth-first search (BFS) is an algorithm for traversing or searching
tree or graph data structures. It starts at the tree root
(or some arbitrary node of a graph, sometimes referred to as a 'search key')
and explores the neighbor nodes first, before moving to the next
level neighbors.
http://web.cs.unlv.edu/larmore/Courses/CSC477/bfsDfs.pdf

Breadth-first search can be used to solve many problems in graph theory, for example:

Copying garbage collection, Cheney's algorithm
Finding the shortest path between two nodes u and v,
with path length measured by number of edges (an advantage over depth-first search)[9]
(Reverse) Cuthill–McKee mesh numbering
Ford–Fulkerson method for computing the maximum flow in a flow network
Serialization/Deserialization of a binary tree vs serialization in sorted order,
allows the tree to be re-constructed in an efficient manner.
Construction of the failure function of the Aho-Corasick pattern matcher.
Testing bipartiteness of a graph.
"""
from graph.graph_base import Graph
from graph.vertex import Vertex


def bfs_undirected_cyclic(graph: Graph, start: Vertex):
    """
    implementation of Breath-First-search algorithm for
    undirected cyclic graph
    - visit all nodes reachable from ${start}
    - (V+E) time (V - count of vertexes; E count of edges)
    - avoid duplicates

    graph - instance of class of Graph type
    start - id or instance of Vertex class

    *returns* all nodes reach from given ${start} and their levels
    """
    if not isinstance(graph, Graph):
        return None, None
    start_vertex = graph.get_vertex(start)
    if not start_vertex:
        return None, None
    level = {start_vertex: 0}
    parent = {start_vertex: None}
    i = 1
    frontier = [start_vertex]
    while frontier:
        _next = []
        for parent_vertex in frontier:
            for child_id in parent_vertex.adj:
                child_vertex = parent_vertex.adj[child_id]
                if child_vertex not in level and child_vertex:
                    level[child_vertex] = i
                    parent[child_vertex] = parent_vertex
                    _next.append(child_vertex)
        frontier = _next
        i += 1
    return level, parent


def get_shortest_path(graph: Graph, start: Vertex, end: Vertex):
    """
    find shortest path between two vertices of graph

    * graph - instance of class of Graph type
    * start - start point (id or instance of Vertex class)
    * end   - end point (id or instance of Vertex class)

    returns shortest path between ${start} and ${end}
    """
    if not isinstance(graph, Graph):
        return None
    start_vertex = graph.get_vertex(start)
    end_vertex = graph.get_vertex(end)
    bfs = bfs_undirected_cyclic(graph, start_vertex)
    parent = bfs[1]
    if parent is None:
        return []
    result = [end_vertex]
    current = end_vertex
    if current not in parent:
        return []
    while parent[current] is not None:
        current = parent[current]
        result.append(current)
    return result
