# !/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2020 Vladimir Shurygin.  All rights reserved.
#
"""
TimSort is a sorting algorithm based on Insertion Sort and Merge Sort.

A stable sorting algorithm works in O(n Log n) time
Used in Java’s Arrays.sort() as well as Python’s sorted() and sort().
First sort small pieces using Insertion Sort, then merges the pieces using merge of merge sort.
We divide the Array into blocks known as Run. We sort those runs using insertion sort one by one and then merge those
runs using combine function used in merge sort. If the size of Array is less than run, then Array get sorted just
by using Insertion Sort. The size of run may vary from 32 to 64 depending upon the size of the array.

Note that merge function performs well when sizes subarrays are powers of 2.
The idea is based on the fact that insertion sort performs well for small arrays.

Details of below implementation :

We consider size of run as 32.
We one by one sort pieces of size equal to run
After sorting individual pieces, we merge them one by one. We double the size of merged subarrays after every iteration.

Links
https://www.geeksforgeeks.org/timsort/
https://svn.python.org/projects/python/trunk/Objects/listsort.txt
"""

# Python3 program to perform TimSort.
RUN = 32


def insertion_sort(arr, left, right):
    """This function sorts array from left index
    to to right index which is of size atmost RUN"""
    for i in range(left + 1, right + 1):

        temp = arr[i]
        j = i - 1
        while arr[j] > temp and j >= left:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp


def merge(arr, l, m, r):
    """merge function merges the sorted runs"""
    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
    i, j, k = 0, 0, l
    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    # copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
    # copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


def tim_sort(arr):
    """iterative Timsort function to
    sort the array[0...n-1] (similar to merge sort)  """
    n = len(arr)
    # Sort individual subarrays of size RUN
    for i in range(0, n, RUN):
        insertion_sort(arr, i, min((i + 31), (n - 1)))
    # start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = RUN
    while size < n:
        # pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):
            # find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))
            # merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            merge(arr, left, mid, right)
        size = 2 * size


if __name__ == '__main__':
    arr = [5, 21, 7, 23, 19]
    print(arr)
    tim_sort(arr)
    print(arr)
