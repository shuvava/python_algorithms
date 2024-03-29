''' This class is a base implementation of any algorithm programm
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
    ''' this class implements base functionlaty on any algoruthm programm
    '''
    @abc.abstractmethod
    def set_console_args(self, parser):
        ''' adds console parameters  into ArgumentParser object'''
        return parser

    def get_context(self):
        ''' Creats excution context command line args
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
        self.set_console_args(parser)
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
        *list of list* - List of words if file was readed of empty list
        '''
        data = []
        if not path.exists(file_name):
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
            for line in lines:
                data.append(line.split())
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
        _filename = self.context.file
        if self.context.length > 0:
            _data = self.__gen_array(self.context.length, 10 * self.context.length)
            if _filename:
                self._save_file(_filename, _data)
        else:
            if not _filename:
                _data = self.__gen_array(DEFAULT_LENGTH, 10 * DEFAULT_LENGTH)
            else:
                _data = self._read_file(_filename)[0]
        length = len(_data)
        _result = (_data[random.randrange(0, length)], _data)
        if self.verbosity:
            print(_result)
        return _result

    @abc.abstractmethod
    def main(self):
        '''Algorithm implementation '''
        raise NotImplementedError('algorithm should be implemented')

    def run(self):
        ''' run alorithm and checks results'''
        _result = '{}_results'.format(self._main)
        cProfile.runctx('self.main()', globals(), locals(), _result)
        print('------------------------------------------')
        _stat = pstats.Stats(_result)
        _stat.strip_dirs().sort_stats(-1).print_stats(self._main)
        #_stat.strip_dirs().sort_stats(-1).print_stats()
