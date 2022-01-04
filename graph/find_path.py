#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2017-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
Find shortest path in graph
'''
import os
from sys import path

path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../common')))

from base_graph import BaseGraph


class FindPathGraph(BaseGraph):
    def find_all_paths(self, start_index, end_index, _path=[]):
        '''Finds all possible ways between vertexes of graph 

        :Parameters:
        start_index: *number* start index of path
        end_index: *number* end index of path
        _path: *list* current building path

        :Returns:
        *list* all possible paths
        '''
        _path = _path + [start_index]  # create new copy of path
        if start_index == end_index:
            return [_path]
        if start_index > self.get_nodes_len():
            return []
        paths = []
        edges = self.get_edges(True)
        for edge in edges[start_index]:
            newpaths = self.find_all_paths(edge[1], end_index, _path)
            for newpath in newpaths:
                paths.append(newpath)
        return paths

    def main(self):
        '''main entry point'''
        start_inx = self._get_node_index(7)
        end_inx = self._get_node_index(9)
        paths_inx = self.find_all_paths(start_inx, end_inx)
        paths = []
        for path_inx in paths_inx:
            paths.append(self.get_nodes_sequence(path_inx))
        print(paths)


if __name__ == '__main__':
    FindPathGraph().run()
