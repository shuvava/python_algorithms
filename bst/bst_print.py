'''
console print of BST
'''

from bst_node import Node

def _print_tree(node, with_values=True):
    '''Recursive function used for pretty-printing the binary tree.
    In each recursive call, a "box" of characters visually representing the
    current subtree is constructed line by line. Each line is padded with
    whitespaces to ensure all lines have the same length. The box, its width,
    and the start-end positions of its root (used for drawing branches) are
    sent up to the parent call, which then combines left and right sub-boxes
    to build a bigger box etc.'''
    if not isinstance(node, Node):
        return [], 0, 0, 0
    if with_values:
        node_repr = str(node.value)
    else:  # pragma: no cover
        node_repr = 'O'
    line1 = []
    line2 = []
    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths and their root positions
    l_box, l_box_width, l_root_start, l_root_end = \
        _print_tree(node.left, with_values)
    r_box, r_box_width, r_root_start, r_root_end = \
        _print_tree(node.right, with_values)

    # Draw the branch connecting the new root to the left sub-box,
    # padding with whitespaces where necessary
    if l_box_width > 0:
        l_root = -int(-(l_root_start + l_root_end) / 2) + 1  # ceiling
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the new root
    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    # Draw the branch connecting the new root to the right sub-box,
    # padding with whitespaces where necessary
    if r_box_width > 0:
        r_root = int((r_root_start + r_root_end) / 2)  # floor
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root + 1))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = ' ' * gap_size
    new_box = [''.join(line1), ''.join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root positions
    return new_box, len(new_box[0]), new_root_start, new_root_end


def bst_print(node = None, with_values=True):
    '''print BST
    
    :Parameters:
    node: *Node* - start node of printing tree (*default root node*)
    with_values: *Boolean* - print value of element in array(*default True*)
    ''' 
    if not isinstance(node, Node):
        return ''
    tree_str_ = '\n' + '\n'.join(_print_tree(node, with_values)[0])
    print(tree_str_)