''' Implementation of sentinel linear search
page 16 of Algorithms Unlocked(2013)
Author Vlad Shurygin 09/18/2017
'''

from base_interface import BaseAlg

class Linear(BaseAlg):
    ''' Implematation of sentinel linear search'''
    def set_console_args(self, parser):
        ''' adds console parameters  into ArgumentParser object'''
        return parser

    @staticmethod
    def search(array, x):
        '''sentinel-linear-search implementation
        Parameters
        ----------
        array: list
            array of elements to search
        x: int element to find
        Returns
        -------
            index of element 'x' in lint 'array'
        '''
        last = array[-1]
        array[-1] = x
        i = 0
        n = len(array)
        while array[i] != x:
            i += 1
        array[-1] = last
        if i < n or array[-1] == x:
            return i
        return None

    def main(self):
        '''main entry point'''
        _x, _t = self.get_array()
        result = self.search(_t, _x)
        print('------------------------------------------')
        print(result, _t[result])

runner = Linear()
runner.run()
