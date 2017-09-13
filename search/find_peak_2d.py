'''Find a peak if it exists
a peak if and only if b ≥ a and b ≥ c. Position 9 is a peak if i ≥ h.
'''
import os
import argparse
DEFAULT_FILE = 'find_peak_2d.txt'

def get_context():
    ''' Creats excution context command line args
    Returns
    -------
    Object
        object with command line arguments
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="file name with sample data")
    parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
    return parser.parse_args()

def read_file(file_name, verbosity=False):
    """ Reads files content and split on words

    Parameters
    ----------
    file_name : string
        full or relative path to the file
    verbosity: Boolean
        show verbose output

    Returns
    -------
    List of List
        List of words if file was readed of empty list
    """
    data = []
    if not os.path.exists(file_name):
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
        for line in lines:
            data.append(line.split())
        return data

def find_a_peak_1d(arr, offset=0, verbosity=False):
    """ Finds a one dimension peak
    Parameters
    ----------
    list : List
        Array of integers
    verbosity: Boolean
        show verbose output

    Returns
    -------
    Tuple(Integer, Integer)
        Index of a peak and value
    """
    index = int(round(len(arr)/2))
    if verbosity:
        print(arr)
        print('arr[0:index]={}; arr[index+1:len(arr)]={}'.format( \
            arr[0:index], arr[index+1:len(arr)]))
        print('app[index]={}; index={}; len/2={}; len ={}; offset={}'.format( \
            arr[index], index, len(arr)/2, len(arr), offset))
    if index >= 1 and arr[index] < arr[index-1]:
        return find_a_peak_1d(arr[0:index], offset, verbosity)
    if index+1 < len(arr) and arr[index] < arr[index+1]:
        return find_a_peak_1d(arr[index+1:len(arr)], offset+index+1, verbosity)
    if index >= 1 and index+1 < len(arr) and arr[index] == arr[index-1] and arr[index] == arr[index+1]:
        left = find_a_peak_1d(arr[0:index], offset, verbosity)
        right = find_a_peak_1d(arr[index+1:len(arr)], offset+index+1, verbosity)
        if left[1]> right[1]:
            return left
        return right
    return (offset+index, arr[index])


def get_row(dataset, row):
    '''return row from dataset
    Parameters
    ----------
    dataset: list of list
    row: Integer 
        Number of rows to return

    Returns
    -------
        list of words
    '''
    return list(zip(*dataset))[row]

CONTEXT = get_context()

if not CONTEXT.file:
    CONTEXT.file = DEFAULT_FILE
DATASETS = read_file(CONTEXT.file, CONTEXT.verbosity)
index_row = 0
result_row = int(round(len(DATASETS)/2))
while (index_row  != result_row):
    index_row = result_row
    row = DATASETS[index_row]
    if CONTEXT.verbosity:
        print('-----------------------------------')
    result = find_a_peak_1d(row, verbosity=CONTEXT.verbosity)
    index_column = result[0]
    if CONTEXT.verbosity:
        print('    a peak = {}'.format(result))
        print('-----------------------------------')
    column = get_row(DATASETS, index_column)
    result = find_a_peak_1d(column, verbosity=CONTEXT.verbosity)
    result_row = result[0]
    if CONTEXT.verbosity:
        print('    a peak = {}'.format(result))
        print('-----------------------------------')

print('row={};column={};value={}'.format(index_row, index_column, DATASETS[index_row][index_column]))
