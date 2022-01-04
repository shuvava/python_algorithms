#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2019-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class Node:
    def __init__(self, id):
        self.id = id
        self.adj = set()

    def add_adj(self, item):
        if not isinstance(item, Node):
            return
        self.adj.add(item)


def build_tree(board_len):
    tree = []
    inx = 0
    while inx < board_len:
        nodeA = Node(f'{inx}A')
        nodeB = Node(f'{inx}B')
        nodeA.add_adj(nodeB)
        nodeB.add_adj(nodeA)
        if inx > 0:
            nodeA.add_adj(tree[-2])
            tree[-2].add_adj(nodeA)
            nodeB.add_adj(tree[-1])
            tree[-1].add_adj(nodeB)
        tree.append(nodeA)
        tree.append(nodeB)
        inx += 1
    return tree


def find_path(start, end, paths, visited, path):
    visited.add(start.id)
    path.append(start.id)
    if start == end:
        # print(path)
        paths.append(list(path))
    else:
        for node in start.adj:
            if node.id not in visited:
                find_path(node, end, paths, visited, path)
    path.pop()
    visited.remove(start.id)


def find_all_paths(start, end):
    '''https://www.geeksforgeeks.org/find-paths-given-source-destination/
    '''
    paths = []
    visited = set()
    path = []
    find_path(start, end, paths, visited, path)
    return paths


if __name__ == '__main__':
    _tree = build_tree(4)
    _start = _tree[0]
    _end = _tree[-1]
    ids = [item.id for item in _tree]
    print(ids)
    print('------------')
    _paths = find_all_paths(_start, _end)
    for idx, val in enumerate(_paths):
        print(f'{idx}   {val}')
