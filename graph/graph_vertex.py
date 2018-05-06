'''
graph vertex - ie node of graph
vertex (plural vertices) or node is the fundamental unit of which graphs are formed:
an undirected graph consists of a set of vertices and a set of edges
(unordered pairs of vertices), while a directed graph consists of a set of vertices
and a set of arcs (ordered pairs of vertices)
'''

class Vertex(object):
    '''node of graph
    '''
    def __init__(self, id, adjacency_list={}, properties={}):
        self.__id = id
        self.__adjacency_list = adjacency_list
        self.__properties = properties

    @property
    def id(self):
        return self.__id

    @property
    def adj(self):
        return self.__adjacency_list

    @property
    def properties(self):
        return self.__properties

    def add_adjacency(self, node):
        if not isinstance(node, Vertex):
            return
        if node.id in self.__adjacency_list:
            return
        self.__adjacency_list[node.id]=node
