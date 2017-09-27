'''Implementation of Recursive-linear-search
Procedure RECURSIVE-LINEAR-SEARCH.A; n; i; x/
Inputs: Same as LINEAR-SEARCH, but with an added parameter i .
Output: The index of an element equaling x in the subarray from AOEi
through AOEn, or NOT-FOUND if x does not appear in this subarray.
1. If i > n, then return NOT-FOUND.
2. Otherwise (i  n), if AOEi D x, then return i .
3. Otherwise (i  n and AOEi ¤ x), return
RECURSIVE-LINEAR-SEARCH.A; n; i C 1; x/.
'''
from base_interface import BaseAlg

class Linear(BaseAlg):
    ''' Implematation of sentinel linear search'''
    def set_console_args(self, parser):
        ''' adds console parameters  into ArgumentParser object'''
        return parser

    @staticmethod
    def search(array, x, i=0, ln=0):
        '''Recursive-linear-search implementation
        Parameters
        ----------
        array: list
            array of elements to search
        x: int element to find
        i: current position in array
        ln: length of array if 0 need to calculate
        Returns
        -------
            index of element 'x' in lint 'array'
        '''
        if ln == 0:
            ln = len(array)
        if i > ln:
            return None
        if array[i] == x:
            return i
        return Linear.search(array, x, i+1, ln)

    def main(self):
        '''main entry point'''
        _x, _t = self.get_array()
        result = self.search(_t, _x)
        print('------------------------------------------')
        print(result, _t[result])

runner = Linear()
runner.run()
