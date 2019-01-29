#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
#
from heapq import heappush, heappop
from graph_base import Graph
from fn_graph import load_graph

def single_path(graph, start, end):
    '''implementation of dijkstra algorithm with priority queue
    '''
    if not isinstance(graph, Graph):
        return None
    start_vertex = graph.get_vertex(start)
    if not start_vertex:
        return None
    end_vertex = graph.get_vertex(end)
    if not end_vertex:
        return None
    visited = {start_vertex:(0, None)}
    pq = [(0, start_vertex)]
    while pq:
        pq_vertex = heappop(pq)
        vertex = pq_vertex[1]
        weight = visited[vertex][0]
        for child_id, child_vertex in vertex.adj.items():
            adj_weight = vertex.weights[child_id]
            if child_vertex in visited:
                current_weight = visited[child_vertex][0]
                if current_weight > adj_weight + weight:
                    visited[child_vertex] = (adj_weight + weight, vertex)
            else:
                heappush(pq, (adj_weight + weight, child_vertex))
                visited[child_vertex] = (adj_weight + weight, vertex)
    if end_vertex not in visited:
        return None
    result = [end_vertex.id]
    vertex = end_vertex
    weight = visited[end_vertex][0]
    while vertex != start_vertex:
        vertex = visited[vertex][1]
        result.append(vertex.id)
    result.reverse()
    return (weight, result)




if __name__ == '__main__':
    _graph = load_graph('dijkstras.json', True)
    #_result = single_path(_graph, 1, 3)
    _result = single_path(_graph, 2, 4)
    print(f'path weight = {_result[0]}; path = {_result[1]}')
