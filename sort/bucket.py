#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
bucket sort prerequisites: 
 - hash function that is used to partition the elements 
   must be very good and must produce ordered hash: 
     if the i < j then hash(i) < hash(j)

cket sort is actually very good considering that counting sort is reasonably
 equal to its upper bound and counting sort

https://javarevisited.blogspot.com/2017/01/bucket-sort-in-java-with-example.html#ixzz5qyOq0oJo

complexity O(n)
'''
def get_hash(i, prime):
    return i * prime


def bucket_sort(arr):
    _len = len(arr)
    if _len <2:
        return arr # already sorted
    _max = max(arr) #O(n)
    buckets = [None]*(_len**2)
    prime = (_len**2-1)//_max
    for i in arr: # O(n)
        _hash = get_hash(i, prime)
        if buckets[_hash] is None:
            buckets[_hash] = []
        buckets[_hash].append(i)
    res = []
    for bucket in buckets:#O(n)
        if bucket is not None:
            res.extend(bucket)
    return res

if __name__ == '__main__':
    arr = [8,5,3,1,9,6,0,7,4,2,5]
    res = bucket_sort(arr)
    print(res)
