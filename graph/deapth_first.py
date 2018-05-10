'''
implementation of Depth-First algorithm
Depth-first search (DFS) is an algorithm for traversing or searching
tree or graph data structures. One starts at the root 
(selecting some arbitrary node as the root in the case of a graph) 
and explores as far as possible along each branch before backtracking.
'''
from undirected_cyclic import Graph

def dfs_undirected_cyclic(graph, start, visited=None):
    '''implementation of Depth-First-search algorithm for
    undirected cyclic graph

    graph - instance of class of Graph type
    start - id or instance of Vertex class

    *returns* all nodes reach from given ${start} and their levels
    '''
    if not isinstance(graph, Graph):
        return (None, None)
    start_vertex = graph.get_vertex(start)
    if not start_vertex:
        return (None, None)
    level = {start_vertex: 0}
    parent = {start_vertex: None}
    i = 1
    stack = [start_vertex]
    while stack:
        current_vertex = stack.pop()
        for child_id in current_vertex.adj:
            child_vertex = current_vertex.adj[child_id]
            if child_vertex not in level and child_vertex:
                level[child_vertex] = level[current_vertex] + 1
                parent[child_vertex] = current_vertex
                stack.append(child_vertex)
    return (level, parent)
    

