import random
from os import path

DEFAULT_LENGTH = 10


def _print_tree(heap, index, with_ids=False, with_values=True):
    """Recursive function used for pretty-printing the binary tree.
    In each recursive call, a "box" of characters visually representing the
    current subtree is constructed line by line. Each line is padded with
    whitespaces to ensure all lines have the same length. The box, its width,
    and the start-end positions of its root (used for drawing branches) are
    sent up to the parent call, which then combines left and right sub-boxes
    to build a bigger box etc."""
    if not heap.array or index is None or index < heap.root_index():
        return [], 0, 0, 0
    if with_ids and with_values:
        node_repr = '{}:{}'.format(index, heap.array[index])
    elif with_ids and not with_values:
        node_repr = str(index)
    elif not with_ids and with_values:
        node_repr = str(heap.array[index])
    else:  # pragma: no cover
        node_repr = 'O'
    line1 = []
    line2 = []
    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths and their root positions
    l_box, l_box_width, l_root_start, l_root_end = \
        _print_tree(heap, heap.left(index), with_ids, with_values)
    r_box, r_box_width, r_root_start, r_root_end = \
        _print_tree(heap, heap.right(index), with_ids, with_values)

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


def print_tree(heap, index=0, with_ids=False, with_values=True):
    '''print BTS tree starting from index
    
    :Parameters:
    index: *Number* - start index of printing tree
    with_ids: *Boolean* - print index of element in array (*default False*)
    with_values: *Boolean* - print value of element in array(*default True*)
    '''
    tree_str_ = '\n' + '\n'.join(_print_tree(heap, index, with_ids, with_values)[0])
    print(tree_str_)


def __gen_array(length, max_value=1000):
    '''Generates random array
    Parameters
    ----------
    length: int
        the length of random array
    Returns
    -------
        list of random elements
    '''
    _data = []
    _i = 0
    while _i < length:
        _data.append(random.randrange(1, max_value))
        _i += 1
    return _data


def _save_file(file_name, data, verbosity=False):
    '''save data into file name

    :Parameters:
    filename: *String* name of the file to store data
    data: *list* data to save'''
    if verbosity:
        print('saving into file {}'.format(file_name))
    try:
        file = open(file_name, 'w')
    except PermissionError:
        print('unable to save the file')
    else:
        with file:
            file.write(' '.join(map(str, data)))
        file.close()


def _read_file(file_name, verbosity=False):
    ''' Reads files content and split on words

    :Parameters:
    file_name: *string* - full or relative path to the file
    verbosity: *Boolean* - show verbose output

    :Returns:
    *list of list* - List of words if file was read of empty list
    '''
    data = []
    if not path.exists(file_name):
        data.append([])
        return data
    if verbosity:
        print('reading file {}'.format(file_name))
    try:
        file = open(file_name, 'r')
    except PermissionError:
        print('unable to read the file')
    else:
        with file:
            lines = file.read().splitlines()
            if not lines: # empty file
                data.append([])
                return data
        for line in lines:
            data.append([int(s) for s in line.split()])
        return data


def get_array(file_name=None, length=DEFAULT_LENGTH, verbosity=False):
    '''Generate random array or load it from file
    '''
    _filename = ''
    if file_name is not None:
        _filename = file_name.strip()
    if length > 0:
        _data = __gen_array(length, 10 * length)
        if _filename:
            _save_file(_filename, _data, verbosity)
    else:
        if not _filename:
            _data = __gen_array(DEFAULT_LENGTH, 10 * DEFAULT_LENGTH)
        else:
            _data = _read_file(_filename, verbosity)[0]
    if verbosity:
        print(_data)
    return _data


def get_min_value_id(itemA_id, itemA_val, itemB_id, itemB_val):
    if itemA_id is None:
        return itemB_id
    if itemB_id is None:
        return itemA_id
    if itemA_val is None:
        return itemB_id
    if itemB_val is None:
        return itemA_id
    if itemA_val < itemB_val:
        return itemA_id
    return itemB_id


def get_max_value_id(itemA_id, itemA_val, itemB_id, itemB_val):
    if itemA_id is None:
        return itemB_id
    if itemB_id is None:
        return itemA_id
    if itemA_val is None:
        return itemB_id
    if itemB_val is None:
        return itemA_id
    if itemA_val > itemB_val:
        return itemA_id
    return itemB_id