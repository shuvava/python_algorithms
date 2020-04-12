#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#

from bst_heap_base import BaseHeap
from bst_heap_utils import get_max_value_id

class MaxHeap(BaseHeap):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def heapify(self, index=None, max_index = None):
        '''correct a single violation of the heap property in a subtree at its root
        :Heap Property: *The key of a node is >= than the keys of its children*
        
        :param index: index of element (*default None == Root element of heap*)
        :type index: Number
        '''
        if not self.array:  # empty array
            return
        if index is None or index < self.root_index():  # fix the first element
            index = self.root_index()
        #init variables
        left = self.left(index, max_index)
        right = self.right(index, max_index)
        largest = index

        largest = get_max_value_id(left, self.get_value(left), largest, self.get_value(largest))
        largest = get_max_value_id(right, self.get_value(right), largest, self.get_value(largest))
        # if left is not None and self.get_value(left) > self.get_value(index):
        #     largest = left
        # if right is not None and self.get_value(right) > self.get_value(largest):
        #     largest = right
        if largest != index:# fix heap and do recursive call
            self.swap(index, largest)
            self.heapify(largest, max_index)
