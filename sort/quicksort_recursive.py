#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
#
'''QuickSort
Complexity: O(n*ln(n)); Worst: O(n2)
Algorithm:
    1. Partition array -> choose pivot element
         put in the left array elements smaller pivot
         put in the left array elements bigger pivot
'''

def partition(A, start_inx, end_inx):
    '''Rearranges the elements of array[start:end] so that every element in
        array[start:pivot] is less than or equal to array[pivot] and every element in
        array[pivot:end] is greater than array[pivot]. Returns the index pivot to the caller
    '''
    pivot = inx = start_inx
    while inx < end_inx:
        if A[inx] <= A[end_inx]:
            A[pivot], A[inx] = A[inx], A[pivot]
            pivot += 1
        inx += 1
    A[pivot], A[end_inx] = A[end_inx], A[pivot]
    return pivot

def quicksort(A, start_inx, end_inx):
    if end_inx <= start_inx:
        return
    middle = partition(A, start_inx, end_inx)
    quicksort(A, start_inx, middle-1)
    quicksort(A, middle+1, end_inx)
    return A

if __name__ == '__main__':
    arr = [6, 5, 3, 2, 8, 10, 9]
    print(arr)
    result = quicksort(arr, 0, len(arr)-1)
    print(result)
