'''
Base graph class
'''
import abc
from vertex import Vertex

class Graph(object, metaclass=abc.ABCMeta):
    def __init__(self, directed, cyclic):
        self.__is_directed = directed
        self.__is_cyclic = cyclic
        self.vertexes = {}

    @property
    def directed(self):
        return self.__is_directed

    @property
    def cyclic(self):
        return self.__is_cyclic

    def add_vertex(self, node):
        if not isinstance(node, Vertex):
            return
        if node.id in self.vertexes:
            return
        self.vertexes[node.id] = node

    def get_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            _id = vertex.id
        else:
            _id = str(vertex)
        if _id not in self.vertexes:
            return None
        return self.vertexes[_id]

    @abc.abstractmethod
    def add_adjacency(self, node_parent, node_child):
        raise NotImplementedError('method should be implemented')
