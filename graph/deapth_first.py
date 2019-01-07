'''
implementation of Depth-First algorithm
Depth-first search (DFS) is an algorithm for traversing or searching
tree or graph data structures. One starts at the root 
(selecting some arbitrary node as the root in the case of a graph) 
and explores as far as possible along each branch before backtracking.
http://web.cs.unlv.edu/larmore/Courses/CSC477/bfsDfs.pdf
'''
from graph_base import Graph

def dfs_undirected_cyclic(graph, start):
    '''implementation of Depth-First-search algorithm for
    undirected cyclic graph. Def can have multiple copies on
    the stack at the same time. However, the total number of
    iterations of the innermost loop of Def cannot exceed
    the number of edges of G, and thus the size of S cannot exceed m.
    The running time is O(n + m).
    - (V+E) time (V - count of vertexes; E count of edges)

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

def dfs_undirected_cyclic_b(graph, start):
    '''implementation of Depth-First-search algorithm for
    undirected cyclic graph. 
    No vertex can be on the stack in more than one place.
    The size of S is thus not more than n.
    The time complexity is O(n + m).
    - (V+E) time (V - count of vertexes; E count of edges)

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
    stack = [start_vertex]
    while stack:
        current_vertex = stack.pop()
        for child_id in current_vertex.adj:
            child_vertex = current_vertex.adj[child_id]
            if child_vertex not in level and child_vertex:
                level[child_vertex] = level[current_vertex] + 1
                parent[child_vertex] = current_vertex
                stack.append(current_vertex)
                stack.append(child_vertex)
                break
    return (level, parent)

def dfs_detect_cycle(graph, start):
    if not isinstance(graph, Graph):
        return (None, None)
    start_vertex = graph.get_vertex(start)
    if not start_vertex:
        return (None, None)
    level = {start_vertex: 0}
    stack = [start_vertex]
    while stack:
        current_vertex = stack.pop()
        for child_id in current_vertex.adj:
            child_vertex = current_vertex.adj[child_id]
            if child_vertex not in level and child_vertex:
                level[child_vertex] = level[current_vertex] + 1
                stack.append(child_vertex)
            else:
                return True
    return False