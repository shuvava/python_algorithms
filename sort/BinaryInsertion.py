'''Binary Insertion sort
general insertion sort spend most of the time 
on looking up the right place to insert element
we can improve in using binary search alorithm 
to loking for the right place 
'''
#add parent directory with base module
import os
from sys import path

path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../common')))

from base_interface import BaseAlg

class BSort(BaseAlg):
    @staticmethod
    def swap(array, _inx1, _inx2):
        '''this method was intensionally made separate to evaluate conut of calls'''
        array[_inx1], array[_inx2] = array[_inx2], array[_inx1]

    @staticmethod
    def bianry_search(arr, crt_inx, _inx, offset=0):
        '''Do insertion of the element in the right spot'''
        if crt_inx == 0:
            return 0 # degenerate case
        index = int(round((_inx-offset)/2))
        if arr[crt_inx] == arr[index]:
            return index
        #boundary cases
        if index == 0 and arr[crt_inx] < arr[0]:
            return 0 # looking value is the lowest
        if index == crt_inx-1 and arr[crt_inx] > arr[index]:
            return index # looking value is the biggest
        if arr[crt_inx] < arr[index]:
            return BSort.bianry_search(arr, crt_inx, index, offset)
        return BSort.bianry_search(arr, crt_inx, _inx, index)
        # lkp = _inx-1
        # tmp_inx = _inx
        # while lkp >= 0:
        #     if array[tmp_inx] < array[lkp]:
        #         InsertionSort.swap(array, tmp_inx, lkp)
        #         tmp_inx = lkp
        #     else:
        #         break
        #     lkp -= 1

    @staticmethod
    def sort(array):
        '''Implementation of Insertion sort algorithm'''
        arr_ln = len(array)
        if arr_ln < 2:
            return #already sorted
        inx = 1
        while inx < arr_ln:
            BSort.insertion(array, inx)
            inx += 1

    def main(self, _array):
        '''main entry point'''
        self.sort(_array)
        if self.verbosity:
            print('------------------------------------------')
            print(_array)

runner = BSort()
runner.run()
