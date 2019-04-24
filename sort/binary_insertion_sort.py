#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
BINARY-INSERTION-SORT (A, n) => A[1 . . n] 
     for j ← 2 to n 
           insert key A[j] into the (already sorted) sub-array A[1 .. j-1]. 
           Use binary search to find the right position 


Binary search with take Θ(log n) time.  However, shifting the elements after insertion will  still take Θ(n) time.  Complexity: Θ(n log n) comparisons  Θ (n 2) swaps
'''

def binary_search(alist, key, start, end):
    '''If key is in the list at index p, then return p.
    If there are multiple such keys in the list, then return the index of any one.
    If key is not in the list and a < key < b where a and b are elements in the list, then return the index of a.
    If key is not in the list and key < a where a is the first element in the list, then return -1.
    Only elements with indexes start to end - 1 inclusive are considered.
    '''
    if end - start <= 1:
        if key < alist[start]:
            return start - 1
        else:
            return start
 
    mid = (start + end)//2
    if alist[mid] < key:
        return binary_search(alist, key, mid, end)
    elif alist[mid] > key:
        return binary_search(alist, key, start, mid)
    else:
        return mid

def binary_insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        pos = binary_search(alist, temp, 0, i) + 1
 
        for k in range(i, pos, -1):
            alist[k] = alist[k - 1]
 
        alist[pos] = temp
 
if __name__ == '__main__':
    arr = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    binary_insertion_sort(arr)
    print(arr)
