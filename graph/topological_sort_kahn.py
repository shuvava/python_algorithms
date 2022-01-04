#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2021-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Kahn's algorithm
One of these algorithms, first described by Kahn (1962), works by choosing vertices
in the same order as the eventual topological sort.
First, find a list of "start nodes" which have no incoming edges and insert them into a set S;
 at least one such node must exist in a non-empty acyclic graph.
Then:
    L ← Empty list that will contain the sorted elements
    S ← Set of all nodes with no incoming edge

    while S is not empty do
        remove a node n from S
        add n to L
        for each node m with an edge e from n to m do
            remove edge e from the graph
            if m has no other incoming edges then
                insert m into S

    if graph has edges then
        return error   (graph has at least one cycle)
    else
        return L   (a topologically sorted order)
quiz-task details can be found in https://leetcode.com/problems/alien-dictionary
"""
from collections import defaultdict
from typing import List


def test(words: List[str]) -> str:
    _len = len(words)
    nodes, incoming_edges = defaultdict(set), defaultdict(set)
    roots, non_roots = set(), set()
    # find roots
    prev = None
    for i in range(_len):
        word = words[i]
        if prev is None:
            prev = word
            continue
        _min = min(len(prev), len(word))
        for i in range(_min):
            if prev[i] == word[i]: continue
            if prev[i] not in non_roots: roots.add(prev[i])
            if word[i] in roots: roots.remove(word[i])
            non_roots.add(word[i])
            nodes[prev[i]].add(word[i])
            incoming_edges[word[i]].add(prev[i])
            break
        prev = word
    abc = ""
    # topological sort implemented using Kahn's algorithm
    # https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm
    stack = list(roots)
    while stack:
        node = stack.pop()
        abc += node
        edges = list(nodes[node]) if node in nodes else []
        for m in edges:
            nodes[node].remove(m)
            if len(nodes[node]) == 0: del nodes[node]
            incoming_edges[m].remove(node)
            if len(incoming_edges[m]) == 0:
                stack.append(m)
                del incoming_edges[m]
    if len(nodes) > 0:
        # error case
        # graph has at least one cycle
        return ""
    # a topologically sorted order
    return abc


if __name__ == '__main__':
    test_cases = [
        (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
        (["z", "x"], "zx"),
        (["z", "x", "z"], ""),
        (["aac", "aabb", "aaba"], "cba"),
        (["cca", "ccbb", "ccbc"], "abc"),
    ]
    cnt = 0
    for test_case in test_cases:
        params = test_case[:-1]
        expected = test_case[-1]
        actual = test(*params)
        is_correct = actual == expected
        cnt += 1
        print('.', end='')
        if not is_correct:
            print(f'\n{params} => (actual={actual}) != (expected={expected})')
    print(f'\nchecked {cnt} tests')
