'''
Base implementation of undirected cyclic graph
'''
from .graph_vertex import Vertex

class Graph(object):
    def __init__(self):
        self.__is_directed = False
        self.__is_cyclic = True
        self.vertexes=[]

    @property
    def directed(self):
        return self.__is_directed

    @property
    def cyclic(self):
        return self.__is_cyclic

    def add_vertex(self, node):
        if not isinstance(node, Vertex):
            return
        self.vertexes.append(node)

    def add_adjacency(self, node_parent, node_child):
        if not isinstance(node_parent, Vertex):
            return
        if not isinstance(node_child, Vertex):
            return
        node_parent.add_adjacency(node_child)
        node_child.add_adjacency(node_parent)
