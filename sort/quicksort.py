#!/usr/bin/env python
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2017-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""QuickSort
Complexity: O(n*ln(n)); Worst: O(n2)
Algorithm:
    1. Partition array -> choose pivot element
         put in the left array elements smaller pivot
         put in the left array elements bigger pivot
"""
# add parent directory with base module
import os
from sys import path

path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../common')))

from base_interface import BaseAlg  # pylint: disable=C0413


class QuickSort(BaseAlg):
    """ Implementation of QuickSort
    Thomas H. Cormen Algorithms Unlocked (2013) page 51
    grokking-algorithms-illustrated-programmers-curious 65
    """

    @staticmethod
    def swap(array, _inx1, _inx2):
        """this method was intensionally made separate to evaluate count of calls"""
        array[_inx1], array[_inx2] = array[_inx2], array[_inx1]

    @staticmethod
    def partition(array_, start, end):
        '''Rearranges the elements of array[start:end] so that every element in
        array[start:pivot] is less than or equal to array[pivot] and every element in
        array[pivot:end] is greater than array[pivot]. Returns the index pivot to the caller

        :Parameters:
        array_: *list* - array of elements to sort
        start: *number* - start index of left array
        end: *number* - end right array
        '''
        # Pivot first element in the array
        pivot = array_[start]
        left = start + 1
        right = end
        while 1:
            while left <= right and array_[left] <= pivot:
                left += 1
            while right >= left and array_[right] >= pivot:
                right -= 1
            if right <= left:
                break
            # Exchange items
            QuickSort.swap(array_, left, right)
        # Exchange pivot to the right position
        QuickSort.swap(array_, start, right)
        return right

    def quick_sort_recursive(self, array_, start, end, level=0):
        '''The procedure for quicksort assumes that we can call a procedure
        PARTITION(array, p, r) that partitions the subarray A[p..r], returning the
        index q where it has placed the pivot.

        :Parameters:
        array_: *list* - array of elements to sort
        start: *number* - start index of left array
        end: *number* - end right array
        '''
        if end <= start:
            if self.verbosity:
                print('end loop after {} iteration'.format(level - 1))
            return
        # Get pivot
        middle = self.partition(array_, start, end)
        # Sort left side of pivot
        self.quick_sort_recursive(array_, start, middle - 1, level + 1)
        # Sort right side of pivot
        self.quick_sort_recursive(array_, middle + 1, end, level + 1)

    def quick_sort_iterative(self, array_, start, end):
        '''Interactive implementation of quicksort,
        it use stack to store variables instead of recursive call

        :Parameters:
        array_: *list* - array of elements to sort
        start: *number* - start index of left array
        end: *number* - end right array
        '''
        stack_ = []
        stack_.append((start, end))

        # Main loop pop and push items until stack is empty
        while stack_:
            left, right = stack_.pop()
            middle = self.partition(array_, left, right)
            # If items in the left of the pivot push them to the stack
            if middle - 1 > left:
                stack_.append((left, middle - 1))
            # If items in the right of the pivot push them to the stack
            if middle + 1 < right:
                stack_.append((middle + 1, right))

    def main(self, _array):
        '''main entry point'''
        # self.quick_sort_recursive(_array, 0, len(_array)-1)
        self.quick_sort_iterative(_array, 0, len(_array) - 1)
        if self.verbosity:
            print('------------------------------------------')
            print(_array)


if __name__ == '__main__':
    QuickSort().run()
