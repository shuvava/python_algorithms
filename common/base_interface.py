''' This class is a base implementation of any algorithm program
'''
import abc
import argparse
import random
import cProfile
import pstats
from os import path
import __main__

DEFAULT_LENGTH = 10

class BaseAlg(object, metaclass=abc.ABCMeta):
    ''' this class implements base functionality on any algorithm program
    '''
    def get_context(self):
        ''' Create execution context command line args
        Returns
        -------
        Object
            object with command line arguments '''
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--file", help="file name with sample data")
        parser.add_argument("-l", "--length",\
            help="length of array of sample data",\
            dest="length", type=int,\
            default=0)
        parser.add_argument('-v', '--verbosity',\
            help='increase output verbosity', action='store_true')
        return parser.parse_args()

    def __init__(self):
        self.context = self.get_context()
        self.verbosity = self.context.verbosity
        self._main = path.splitext(path.basename(__main__.__file__))[0]

    def _save_file(self, file_name, data):
        '''save data into file name

        :Parameters:
        filename: *String* name of the file to store data
        data: *list* data to save'''
        if self.verbosity:
            print('saving into file {}'.format(file_name))
        try:
            file = open(file_name, 'w')
        except PermissionError:
            print('unable to save the file')
        else:
            with file:
                file.write(' '.join(map(str, data)))
            file.close()

    def _read_file(self, file_name):
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
        if self.verbosity:
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

    @staticmethod
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

    def get_array(self):
        '''Generate random array or load it from file
        '''
        _filename = ''
        if self.context.file is not None:
            _filename = self.context.file.strip()
        if self.context.length > 0:
            _data = self.__gen_array(self.context.length, 10 * self.context.length)
            if _filename:
                self._save_file(_filename, _data)
        else:
            if not _filename:
                _data = self.__gen_array(DEFAULT_LENGTH, 10 * DEFAULT_LENGTH)
            else:
                _data = self._read_file(_filename)[0]
        if self.verbosity:
            print(_data)
        return _data

    @abc.abstractmethod
    def main(self, _array):
        '''Algorithm implementation '''
        raise NotImplementedError('algorithm should be implemented')

    def run(self):
        ''' run algorithm and checks results'''
        _result = '{}_results'.format(self._main)
        arr = self.get_array()# pylint: disable=W0612
        cProfile.runctx('self.main(arr)', globals(), locals(), _result)
        print('------------------------------------------')
        _stat = pstats.Stats(_result)
        _stat.strip_dirs().sort_stats(-1).print_stats(self._main)
        #_stat.strip_dirs().sort_stats(-1).print_stats()
