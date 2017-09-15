#!/usr/bin/python
''' find doc distnace between documents
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec02.pdf
'''
import cProfile
import pstats
import time
import sys

import os
import argparse
import string
import math
DEFAULT_FILES = ['doc1.txt', 'doc2.txt']
# This uses the 3-argument version of str.maketrans
# with arguments (x, y, z) where 'x' and 'y'
# must be equal-length strings and characters in 'x'
# are replaced by characters in 'y'. 'z'
# is a string (string.punctuation here)
# where each character in the string is mapped
# to None
TRANSLATOR = str.maketrans('', '', string.punctuation)

def get_context():
    ''' Creats excution context command line args
    Returns
    -------
    Object
        object with command line arguments '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files',\
        dest='files', action='store', nargs='+',\
        default=DEFAULT_FILES, help='file name with sample data')
    parser.add_argument('-v', '--verbosity', help='increase output verbosity', action='store_true')
    return parser.parse_args()

def read_file(file_name, verbosity=False):
    ''' Reads files content and split on words

    Parameters
    ----------
    file_name : string
        full or relative path to the file
    verbosity: Boolean
        show verbose output

    Returns
    -------
    List
        List of words if file was readed of empty list '''
    _data = []
    if not os.path.exists(file_name):
        return _data
    if verbosity:
        print('reading file {}'.format(file_name))
    try:
        _file = open(file_name, 'r', encoding='utf8')
    except (IOError, PermissionError):
        print('unable to read the file {}'.format(file_name))
    else:
        with _file:
            _data = _file.read().lower().translate(TRANSLATOR).split()

        return _data

def create_vector(doc_):
    '''Create vector of the cocument
    Parameters
    ----------
    data: list
        list of low case words
    Returns
    -------
        dict
            a vector of the document '''
    result = {}
    for word_ in doc_:
        result[word_] = result.get(word_, 0) + 1
    return result

def get_dot_product(vector1, vector2):
    '''The dot product operation multiplies two vectors to give a scalar number (not a vector).
    Parameters
    ----------
    vector1: dict
        Vector
    vector2: dict
        Vector
    Returns
    -------
        Number
            The dot product of vectors'''
    result = 0
    for key, value in vector1.items():
        result += value* vector2.get(key, 0)
    return result

def get_vector_length(vector):
    '''Calculate length of vector
    Parameters
    ----------
    vector: dict
        Vector
    Returns
    -------
        Number length of the vector '''
    result = 0
    for  value in vector.values():
        result += value*value
    return math.sqrt(result)

def main():
    '''Main calculation function'''
    context = get_context()
    main_doc_vector = None

    for file in context.files:
        data = read_file(file)
        vector = create_vector(data)
        if context.verbosity:
            print('file: {}'.format(file))
            print(data)
            print(vector)
            print('----------------------------')
        if main_doc_vector is None:
            main_doc_vector = vector
            main_doc_vector_len = get_vector_length(vector)
        else:
            dot_product = get_dot_product(main_doc_vector, vector)
            doc_distance = math.acos(dot_product/(main_doc_vector_len*get_vector_length(vector)))
            print('Document distance for file {0} is {1:0.6f} (radians)'.format(file, doc_distance))

cProfile.run('main()', 'cprofile_results')
print('------------------------------------------')
p = pstats.Stats('cprofile_results')
#filter by module name
p.strip_dirs().sort_stats(-1).print_stats('find_doc_distance')
