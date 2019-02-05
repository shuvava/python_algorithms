#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
#
from graph_base import Graph
from fn_graph import load_graph

def bellman_ford(graph, start, end):
    if not isinstance(graph, Graph):
        return None
    start_vertex = graph.get_vertex(start)
    if not start_vertex:
        return None
    end_vertex = graph.get_vertex(end)
    if not end_vertex:
        return None
    visited = {start_vertex.id: (0, None)}
    for _ in range(0, len(graph.vertexes)):
        for vertex in graph.vertexes.values():
            # current vertex weigh
            weight = None
            if vertex.id in visited:
                weight = visited[vertex.id][0]
            # scanning edges
            for edge_id in vertex.adj.keys():
                adj_weight = vertex.weights[edge_id]
                if edge_id in visited:
                    current_weight = visited[edge_id][0]
                    if weight and current_weight > adj_weight + weight:
                        visited[edge_id] = (adj_weight + weight, vertex.id)
                elif weight is not None:
                    visited[edge_id] = (adj_weight + weight, vertex.id)
    # check for negative cycle
    for vertex in graph.vertexes.values():
        weight = visited[vertex.id][0]
        for edge_id in vertex.adj.keys():
            adj_weight = vertex.weights[edge_id]
            current_weight = visited[edge_id][0]
            if current_weight > adj_weight + weight:
                # negative cycle
                return None
    # restore path
    if end_vertex.id not in visited:
        return None
    result = [end_vertex.id]
    vertex = end_vertex.id
    weight = visited[end_vertex.id][0]
    while vertex != start_vertex.id:
        vertex = visited[vertex][1]
        result.append(vertex)
    result.reverse()
    return (weight, result)

if __name__ == '__main__':
    _graph = load_graph('bellman-ford.json', True)
    _result = bellman_ford(_graph, 0, 3)
    if _result is None:
        print('graph has negative cycle')
    else:
        print(f'path weight = {_result[0]}; path = {_result[1]}')
    # _graph_test = load_graph('dijkstras.json', True)
    # _result = bellman_ford(_graph, 2, 4)
    _graph.vertexes['2'].weights['5'] = 4
    _result = bellman_ford(_graph, 0, 3)
    if _result is None:
        print('graph has negative cycle')
    else:
        print(f'path weight = {_result[0]}; path = {_result[1]}')
