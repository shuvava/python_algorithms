'''Merge sort implementation'''
from base_interface import BaseAlg

class MergeSort(BaseAlg):
    '''Merge sort implementation'''
    @staticmethod
    def sort(array):
        

    def main(self, _array):
        '''main entry point'''
        self.sort(_array)
        if self.verbosity:
            print('------------------------------------------')
            print(_array)

runner = MergeSort()
runner.run()
