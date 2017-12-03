'''
Module implements base read write functionality for json files
'''
import json
from os import path, remove

def read_array_file(file_name, verbosity=False):
    '''Read array of int from space delimetered line in file

    :Parameters:
    file_name: *string* - full or relative path to the file
    verbosity: *bool [default = False]* - show extend info

    :Returns:
    *list of list*
    '''
    data = []
    if not path.exists(file_name):
        data.append([])
        return data
    if verbosity:
        print('reading file {}'.format(file_name))
    try:
        with open(file_name, 'r') as file:
            lines = file.read().splitlines()
            if not lines: # empty file
                data.append([])
                return data
            for line in lines:
                data.append([int(s) for s in line.split()])
            return data
    except PermissionError:
        print('unable to read the file')

def save_array_file(file_name, data, verbosity=False):
    '''Save array of bites into space delimited file

    :Parameters:
    filename: *String* name of the file to store data
    data: *list* data to save
    verbosity: *bool [default = False]* - show extend info
    '''
    if verbosity:
        print('saving into file {}'.format(file_name))
    if not data:
        return
    if not isinstance(data[0], list):
        data = [data]
    try:
        with open(file_name, 'w') as file:
            for items in data:
                file.write(' '.join(map(str, items)))
    except PermissionError:
        print('unable to save the file')

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
        with open(file_name, 'w') as file:
            content = {root: data}
            json.dump(content, file, ensure_ascii=False)
    except PermissionError:
        print('unable to save the file')

def remove_file(file_name, verbosity=False):
    '''delete file'''
    if verbosity:
        print('removing file {}'.format(file_name))
    try:
        remove(file_name)
    except PermissionError:
        print('unable to remove the file')