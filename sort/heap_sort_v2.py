#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2020 Vladimir Shurygin.  All rights reserved.
#
"""
Implementation Heap sort
Running time:
after n iterations the Heap is empty
every iteration involves a swap and a max_heapify
operation; hence it takes O(log n) time

Complexity: O(n*ln(n))
"""
from typing import List


def heapify(unsorted: List[int], index: int, heap_size: int) -> None:
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted: List[int]) -> None:
    """
    Pure implementation of the heap sort algorithm in Python
    :param unsorted: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> heap_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> heap_sort([])
    []

    >>> heap_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    n = len(unsorted)
    # build heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    # sort
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)


if __name__ == '__main__':
    examples = [
        [0, 5, 3, 2, 2],
        [],
        [-2, -5, -45]
    ]
    for example in examples:
        result = f'{example} -> '
        heap_sort(example)
        result += f'{example}'
        print(result)
