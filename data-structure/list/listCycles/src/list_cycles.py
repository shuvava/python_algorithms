#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2019 Vladimir Shurygin.  All rights reserved.
#
'''
find a cycle in a linked list
'''
class LinkedList(object):
    def __init__(self, value):
        self._next = None
        self.value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value


def check_linked_list_cycle(item):
    if not isinstance(item, LinkedList):
        return False
    visited = set()
    _current = item
    _cycle = False
    while _current is not None:
        if _current in visited:
            _cycle = True
            return _cycle
        visited.add(_current)
        _current = _current.next
    return _cycle

def check_linked_list_cycle_floyd(item):
    '''
    Floyd's algorithm. Increment one pointer by one and the other by two.
    If they are ever pointing to the same node, there is a cycle.
    Explanation: https://www.quora.com/How-does-Floyds-cycle-finding-algorithm-work
    '''
    if not isinstance(item, LinkedList):
        return False
    slow = item
    fast = item.next
    while fast is not None and fast.next is not None:
        if fast == slow:
            return True
        fast = fast.next.next
        slow = slow.next
    return False 


if __name__ == '__main__':
    cycled_list = LinkedList(1)
    cycled_list.next = LinkedList(2)
    current = cycled_list.next
    cycle = current
    current.next = LinkedList(3)
    current = current.next
    current.next = LinkedList(4)
    current = current.next
    current.next = cycle
    #result = check_linked_list_cycle(cycled_list)
    result = check_linked_list_cycle_floyd(cycled_list)
    print(f'cycle check result: {result}')