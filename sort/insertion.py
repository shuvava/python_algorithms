'''Insertion sort
for j ← 2 to n
insert key A[j] into the (already sorted) sub-array A[1 .. j-1].
by pairwise key-swaps down to its right position
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec03.pdf
'''
from base_interface import BaseAlg

class InsertionSort(BaseAlg):
    ''' Implematation of insertion sort'''
    @staticmethod
    def swap(array, _inx1, _inx2):
        '''this method was intensionally made separate to evaluate conut of calls'''
        array[_inx1], array[_inx2] = array[_inx2], array[_inx1]

    @staticmethod
    def insertion(array, _inx):
        '''Do insertion of the element in the right spot'''
        lkp = _inx-1
        tmp_inx = _inx
        while lkp >= 0:
            if array[tmp_inx] < array[lkp]:
                InsertionSort.swap(array, tmp_inx, lkp)
                tmp_inx = lkp
            else:
                break
            lkp -= 1

    @staticmethod
    def sort(array):
        '''Implementation of Insertion sort algorithm'''
        arr_ln = len(array)
        if arr_ln < 2:
            return #already sorted
        inx = 1
        while inx < arr_ln:
            InsertionSort.insertion(array, inx)
            inx += 1

    def main(self, _array):
        '''main entry point'''
        self.sort(_array)
        if self.verbosity:
            print('------------------------------------------')
            print(_array)

runner = InsertionSort()
runner.run()
