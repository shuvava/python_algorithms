#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2021-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers,
return any of them. If it is impossible to finish all courses, return an empty array.
Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: [0,1]
    Explanation: There are a total of 2 courses to take. To take course 1 you should have
    finished course 0. So the correct course order is [0,1].
Example 2:
    Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3]
    Explanation: There are a total of 4 courses to take.
    To take course 3 you should have finished both courses 1 and 2.
    Both courses 1 and 2 should be taken after you finished course 0.
    So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:
    Input: numCourses = 1, prerequisites = []
    Output: [0]
Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= numCourses * (numCourses - 1)
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    ai != bi
    All the pairs [ai, bi] are distinct.
"""
from collections import defaultdict, deque
from enum import Enum
from typing import List, Dict, Set


def get_roots(graph: Dict[int, Set]) -> Set[int]:
    """Get roots (nodes with no prerequisites)"""
    roots = set(graph.keys())
    non_roots = set()
    for node, adjs in graph.items():
        for adj in adjs:
            if adj in roots:
                roots.remove(adj)
                non_roots.add(adj)
    return roots


def is_cyclic(graph: Dict[int, Set], roots: Set[int]) -> bool:
    """check if any path from root nodes has cycle"""
    for root in roots:
        visited = set()
        stack = [root]
        while stack:
            _next = []
            for node in stack:
                visited.add(node)
                for adj in graph[node]:
                    if adj in visited:
                        return True
                    _next.append(adj)
            stack = _next
    return False


class NodeState(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3


def topological_sort(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """topological sort
    Geneal algorithm:
        L ← Empty list that will contain the sorted nodes
        while exists nodes without a permanent mark do
            select an unmarked node n
            visit(n)

        function visit(node n)
            if n has a permanent mark then
                return
            if n has a temporary mark then
                stop   (not a DAG)

            mark n with a temporary mark

            for each node m with an edge from n to m do
                visit(m)

            remove temporary mark from n
            mark n with a permanent mark
            add n to head of L
    """
    # Create the adjacency list representation of the graph
    adj_list = defaultdict(list)
    # A pair [a, b] in the input represents edge from b --> a
    for dest, src in prerequisites:
        adj_list[src].append(dest)

    topological_sorted_order = []
    is_possible = True

    # By default all vertces are WHITE
    color = {k: NodeState.WHITE for k in range(numCourses)}

    def dfs(node):
        nonlocal is_possible

        # Don't recurse further if we found a cycle already
        if not is_possible:
            return

        # Start the recursion
        color[node] = NodeState.GRAY

        # Traverse on neighboring vertices
        if node in adj_list:
            for neighbor in adj_list[node]:
                if color[neighbor] == NodeState.WHITE:
                    dfs(neighbor)
                elif color[neighbor] == NodeState.GRAY:
                    # An edge to a GRAY vertex represents a cycle
                    is_possible = False

        # Recursion ends. We mark it as black
        color[node] = NodeState.BLACK
        topological_sorted_order.append(node)

    for vertex in range(numCourses):
        # If the node is unprocessed, then call dfs on it.
        if color[vertex] == NodeState.WHITE:
            dfs(vertex)

    #     Complexity Analysis
    #         Time Complexity: O(V+E) where V represents the number of vertices and
    #         E represents the number of edges.
    #          Essentially we iterate through each node and each vertex in the graph once and only once.
    #     Space Complexity: O(V+E).
    #         We use the adjacency list to represent our graph initially.
    #         The space occupied is defined by the number of edges because for each node as the key,
    #         we have all its adjacent nodes in the form of a list as the value. Hence, O(E)
    #         Additionally, we apply recursion in our algorithm, which in worst case
    #         will incur O(E) extra space in the function call stack.
    #         To sum up, the overall space complexity is O(V+E).
    return topological_sorted_order[::-1] if is_possible else []


def node_indegree(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # Prepare the graph
    adj_list = defaultdict(list)
    indegree = {}
    for dest, src in prerequisites:
        adj_list[src].append(dest)

        # Record each node's in-degree
        indegree[dest] = indegree.get(dest, 0) + 1

    # Queue for maintainig list of nodes that have 0 in-degree
    zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

    topological_sorted_order = []

    # Until there are nodes in the Q
    while zero_indegree_queue:

        # Pop one node with 0 in-degree
        vertex = zero_indegree_queue.popleft()
        topological_sorted_order.append(vertex)

        # Reduce in-degree for all the neighbors
        if vertex in adj_list:
            for neighbor in adj_list[vertex]:
                indegree[neighbor] -= 1

                # Add neighbor to Q if in-degree becomes 0
                if indegree[neighbor] == 0:
                    zero_indegree_queue.append(neighbor)

    return topological_sorted_order if len(topological_sorted_order) == numCourses else []


if __name__ == '__main__':
    test_cases = [
        (2, [[1, 0], [0, 1]], []),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2], [1, 3]], []),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 2, 1, 3]),
        (2, [[1, 0]], [0, 1]),
    ]
    cnt = 0
    for test_case in test_cases:
        params = test_case[:-1]
        expected = test_case[-1]
        actual = topological_sort(*params)
        # actual = node_indegree(*params)
        is_correct = actual == expected
        cnt += 1
        print('.', end='')
        if not is_correct:
            print(f'\n{params} => (actual={actual}) != (expected={expected})')
    print(f'\nchecked {cnt} tests')
