'''
Extend functionality of base_bst module
adding support of modification of BST
'''
from bst_node import Node
from bst_node_query import bst_to_list, bst_next_larger


def bst_fix_node_rank(node, removed_items):
    while node:
        node._rank += removed_items
        node = node.parent


def bst_insert(root_node, node):
    if not isinstance(node, Node):
        return False

    if root_node.value <= node.value:
        if not root_node.right:
            root_node.right = node
            return True
        return bst_insert(root_node.right, node)
    if not root_node.left:
        root_node.left = node
        return True
    return bst_insert(root_node.left, node)

def bst_delete(node):
    if not isinstance(node, Node):
        return
    # save state
    parent = node.parent
    left = node.left
    right = node.right
    is_left_child = node.is_left_child
    is_right_child = node.is_right_child
    children_count = node.children_count
    if children_count == 2:
        next_larger = bst_next_larger(node, node.value)
    # resconnect child elements
    if children_count == 0:
        if is_left_child:
            parent.left = None
        else:
            parent.right = None
    elif children_count == 1:
        if is_left_child:
            parent.left = left or right
        if is_right_child:
            parent.right = left or right
    else:
        # change relationship
        if next_larger.is_left_child:
            next_larger.parent.left = next_larger.right
        else:
            next_larger.parent.right = next_larger.right
        next_larger.parent = None
        if is_left_child:
            parent.left = next_larger
        if is_right_child:
            parent.right = next_larger
        if not (next_larger is left):
            next_larger.left = left
        if not (next_larger is right):
            next_larger.right = right
    del node

#naive implementation of delete
# def bst_delete(node):
#     bst_fix_node_rank(node, -node.rank)
#     if node.is_left_child:
#         node.parent.left = None
#     if node.is_right_child:
#         node.parent.right = None
#     if node.children_count > 0:
#         arr = bst_to_list(node.left, [])
#         bst_to_list(node.right, arr)
#         for value in arr:
#             bst_insert(node.parent, Node(value))
#     del node