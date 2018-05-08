#add parent directory with base module
import os
from sys import path

path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../common')))

from graph_undirect_cyclic import Graph
from graph_vertex import Vertex

from file_operations import read_json_file

def load_undirected_cyclic_graph(data):
    _graph = Graph()
    for _node in data['nodes']:
        properties = {k:v for k,v in _node.items() if k != 'id'}
        vertex = Vertex(_node['id'], properties=properties)
        _graph.add_vertex(vertex)
    for _edge in data['edges']:
        _id = _edge['source']
        vertex = _graph.get_vertex(_id)
        if not vertex:
            next
        targets = _edge['targets']
        for target in targets:
            _graph.add_adjacency(vertex, target)
    return _graph

def load_graph(file_name, verbosity=False):
    data = read_json_file(file_name, 'graph', verbosity)
    if not data['directed'] and data['cyclic']:
        return load_undirected_cyclic_graph(data)
    pass
