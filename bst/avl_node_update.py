'''
Extend functionality of avl module
adding support of rotation of AVL tree
'''
from avl_node import AVL_Node
from bst_node_update import bst_insert, bst_delete

def rotation_left(node):
    if not isinstance(node, AVL_Node):
        return
    if not node.left:
        return
    # save sate
    parent = node.parent
    left = node.left
    right = None
    if node.left.right:
        right = node.left.right
    parent_is_left_child =False
    if parent and node.is_left_child:
        parent_is_left_child = True
    # rotate
    node.parent = None
    left.parent = None
    if parent and parent_is_left_child:
        parent.left = left
    elif parent and not parent_is_left_child:
        parent.right = left
    node.parent = left
    node.left = right
    left.right = node


    return left

def rotation_right(node):
    if not isinstance(node, AVL_Node):
        return
    if not node.right:
        return
    # save sate
    parent = node.parent
    right = node.right
    left = None
    if node.right.left:
        left = node.right.left
    parent_is_left_child =False
    if parent and node.is_left_child:
        parent_is_left_child = True 
    # rotate
    node.parent = None
    right.parent = None
    if parent and parent_is_left_child:
        parent.left = right
    elif parent and not parent_is_left_child:
        parent.right = right
    node.parent = right
    node.right = left
    right.left = node

    return right

def rotation(node):
    if not isinstance(node, AVL_Node):
        return
    if node.left_height > node.right_height:
        # left heavy
        return rotation_left(node)
    if node.right_height > node.left_height:
        # right heavy
        return rotation_right(node)
    # equal => do nothing
    return None

def fix_avl_property(node):
    _node = node
    parent = node.parent
    while parent:
        if not parent.is_valid:
            parent = rotation(parent)
        _node = parent
        parent = parent.parent
    return _node

def avl_insert(root_node, node):
    result = bst_insert(root_node, node)
    if not result:
        return root_node
    # fix_avl_property
    _node = node
    parent = node.parent
    while parent:
        if not parent.is_valid:
            parent = rotation(parent)
        _node = parent
        parent = parent.parent
    return _node

def avl_delete(node):
    parent = node.parent
    if not parent:
        #not implemented deleting the root
        return
    bst_delete(node)
    _parent = parent
    while parent:
        if not parent.is_valid:
            parent = rotation(parent)
        _parent = parent
        parent = parent.parent
    return _parent