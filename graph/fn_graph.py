# add parent directory with base module
import os
from sys import path

path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../common')))

from graph.undirected_cyclic import UndirectedGraph
from graph.directed_cyclic import DirectedGraph
from graph.vertex import Vertex

from file_operations import read_json_file


def __load_graph(_graph, data):
    for _node in data['nodes']:
        properties = {k: v for k, v in _node.items() if k != 'id'}
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


def load_undirected_cyclic_graph(data):
    _graph = UndirectedGraph()
    __load_graph(_graph, data)
    return _graph


def load_directed_cyclic_graph(data):
    _graph = DirectedGraph()
    __load_graph(_graph, data)
    return _graph


def load_graph(file_name, verbosity=False):
    data = read_json_file(file_name, 'graph', verbosity)
    if not data['directed'] and data['cyclic']:
        return load_undirected_cyclic_graph(data)
    elif data['directed'] and data['cyclic']:
        return load_directed_cyclic_graph(data)
    return None
