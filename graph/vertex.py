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
    def __init__(self, vertex_id, adjacency_list=None, properties=None):
        self.__id = str(vertex_id)
        self.__adjacency_list = adjacency_list or {}
        self.__weights = None
        if 'weights' in properties:
            self.__weights = {}
            for weight in properties['weights']:
                self.__weights[str(weight['id'])] = weight['weight']
            del properties['weights']
        self.__properties = properties or {}

    @property
    def id(self):
        return self.__id

    @property
    def weights(self):
        return self.__weights

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
        self.__adjacency_list[node.id] = node
