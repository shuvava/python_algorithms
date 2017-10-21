#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''QuickSort
Complexity: O(n*ln(n)); Worst: O(n2)
Algorithm:
    1. Partition array -> choose pivot element
         put in the left array elements smaller pivot
         put in the left array elements bigger pivot
'''
from base_interface import BaseAlg

class QuickSort(BaseAlg):
    ''' Implementation of QuickSort
    Thomas H. Cormen Algorithms Unlocked (2013) page 67
    grokking-algorithms-illustrated-programmers-curious 65
    '''
    @staticmethod
    def swap(array, _inx1, _inx2):
        '''this method was intensionally made separate to evaluate count of calls'''
        array[_inx1], array[_inx2] = array[_inx2], array[_inx1]

    @staticmethod
    def partition(array, start, end):
        '''Rearranges the elements of array[start:end] so that every element in
        array[start:pivot] is less than or equal to array[pivot] and every element in
        array[pivot:end] is greater than array[pivot]. Returns the index pivot to the caller

        :Parameters:
        array: *list* - array of elements to sort
        start: *number* - start index of left array
        end: *number* - end right array
        '''
        pivot = start
        for inx in range(start, end-1):
            if array[inx] <= array[end]:
                QuickSort.swap(array, pivot, inx)
                pivot += 1
        QuickSort.swap(array, pivot, end)
        return pivot

    def quick_sort(self, array, start, end, level=0):
        '''The procedure for quicksort assumes that we can call a procedure
        PARTITION(array, p, r) that partitions the subarray A[p..r], returning the
        index q where it has placed the pivot.

        :Parameters:
        array: *list* - array of elements to sort
        start: *number* - start index of left array
        end: *number* - end right array
        '''
        if start+1 >= end:
            if self.verbosity:
                print('end loop after {} iteration'.format(level-1))
            return
        middle = self.partition(array, start, end)
        self.quick_sort(array, start, middle, level+1)
        self.quick_sort(array, middle, end, level+1)

    def main(self, _array):
        '''main entry point'''
        self.quick_sort(_array, 0, len(_array)-1)
        if self.verbosity:
            print('------------------------------------------')
            print(_array)

if __name__ == '__main__':
    QuickSort().run()