'''
Extend functionality of base_bst module
adding support of modification of BST
'''
from bst_node import Node
from bst_node_query import bst_to_list


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
            bst_fix_node_rank(root_node, 1)
            return True
        else:
            return bst_insert(root_node.right, node)
    else:
        if not root_node.left:
            root_node.left = node
            bst_fix_node_rank(root_node, 1)
            return True
        else:
            return bst_insert(root_node.left, node)

def bst_delete(node):
    bst_fix_node_rank(node, -node.rank)
    if node.is_left_child:
        node.parent.left = None
    if node.is_right_child:
        node.parent.right = None
    if node.children_count > 0:
        arr = bst_to_list(node.left, [])
        bst_to_list(node.right, arr)
        for value in arr:
            bst_insert(node.parent, Node(value))
    del node