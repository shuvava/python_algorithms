'''
Extend functionality of base_bst module
adding support of look up specific valuer in bst
'''
from bst_node import Node

def _get_node(item):
    node = None
    if isinstance(item, Node):
        node = item
    return node

def bst_find_smaller(item, value):
    '''find first node which value is less or equal value

        :Parameters:
        item: *Node|BST* - node of BST
        value: *Number* - value to search

        :return:
        node: *Node|None* 
    '''
    node = _get_node(item)
    if not isinstance(node, Node):
        return None
    if node.value <= value:
        return node
    return bst_find_smaller(node.left, value)

def bst_count(item, value, _count = 0):
    '''find count of nodes less or equal value in subtree

        :Parameters:
        item: *Node|BST* - node of BST
        value: *Number* - value to search

        :return:
         *Number* count of nodes
    '''
    node = _get_node(item)
    if not isinstance(node, Node):
        return _count
    if node.value <= value:
        _count += 1
        if node.left:
            _count += node.left.rank
        return bst_count(node.right, value, _count)
    else:
        return bst_count(node.left, value, _count)

def bst_max(item):
    '''find max value in bst

        :Parameters:
        item: *Node|BST* - node of BST
    '''
    node = _get_node(item)
    if not isinstance(node, Node):
        return None
    while node:
        max_value = node.value
        node = node.right
    return max_value

def bst_min(item):
    '''find min value in bst

        :Parameters:
        item: *Node|BST* - node of BST
    '''
    node = _get_node(item)
    if not isinstance(node, Node):
        return None
    while node:
        min_value = node.value
        node = node.left
    return min_value

def bst_search(item, value):
    '''find value in bst

        :Parameters:
        item: *Node|BST* - node of BST
        value: *Number* - value to search

        :return:
         *Node|None* found node or None if not found
    '''
    node = _get_node(item)
    if not isinstance(node, Node):
        return None
    if node.value == value:
        return node
    if node.value < value:
        return bst_search(node.right, value)
    return bst_search(node.left, value)

def bst_next_larger(item, value):
    '''find next larger value in bst

        :Parameters:
        item: *Node|BST* - node of BST
        value: *Number* - value to search

        :return:
         *Node|None* found node or None if not found
    '''
    node = _get_node(item)
    if not isinstance(node, Node):
        return None
    if node.value > value:
        node_tmp = bst_next_larger(node.left, value)
        if node_tmp:
            node = node_tmp
        return node
    return bst_next_larger(node.right, value)

def bst_to_list(node, arr=[]):
    if not isinstance(node, Node):
        return arr
    arr.append(node.value)
    bst_to_list(node.left, arr)
    bst_to_list(node.right, arr)
    return arr

