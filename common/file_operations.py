'''
Module implements base read write functionality for json files
'''
import json
from os import path

def read_json_file(file_name, root='bst', verbosity=False):
    ''' Reads JSON file content

    :Parameters:
    file_name: *string* - full or relative path to the file
    root: *string [default = 'bst']* - name of root element
    verbosity: *bool [default = False]* - show extend info

    :Returns:
    *list* - dict of fields of json object
    '''
    if not path.exists(file_name):
        return {}
    if verbosity:
        print('reading file {}'.format(file_name))
    try:
        with open(file_name, 'r') as file:
            content = json.load(file)
            return content[root]
    except PermissionError:
        print('unable to read the file')

def save_json_file(file_name, data, root='bst', verbosity=False):
    '''save data into file name

    :Parameters:
    filename: *String* name of the file to store data
    data: *dict* data to save
    root: *string [default = 'bst']* - name of root element
    verbosity: *bool [default = False]* - show extend info
    '''
    if verbosity:
        print('saving into file {}'.format(file_name))
    try:
        with open(file_name, 'w') as outfile:
            content = {root: data}
            json.dump(content, outfile, ensure_ascii=False)
    except PermissionError:
        print('unable to save the file')