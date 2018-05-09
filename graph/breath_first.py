'''
implementation of Breath-First algorithm
'''
from undirected_cyclic import Graph

def bfs_undirected_cyclic(graph, start):
    '''
    implementation of Breath-First-search algorithm for
    undirected cyclic graph
    - visit all nodes reachable from ${start}
    - (V+E) time (V - count of vertexes; E count of edges)
    - avoid duplicates

    graph - instance of class of Graph type
    start - id or instance of Vertex class

    *returns* all nodes reach from given ${start}
    '''
    if not isinstance(graph, Graph):
        return (None, None)
    start_vertex = graph.get_vertex(start)
    if not start_vertex:
        return (None, None)
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
    return (level, parent)
