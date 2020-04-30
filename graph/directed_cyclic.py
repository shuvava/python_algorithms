"""
Base implementation of directed cyclic graph
"""
from graph.graph_base import Graph
from graph.vertex import Vertex


class DirectedGraph(Graph):
    def __init__(self):
        super().__init__(False, True)

    def add_adjacency(self, node_parent, node_child):
        node_parent = self.get_vertex(node_parent)
        node_child = self.get_vertex(node_child)
        if not isinstance(node_parent, Vertex):
            return
        if not isinstance(node_child, Vertex):
            return
        node_parent.add_adjacency(node_child)
