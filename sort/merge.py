'''Merge sort implementation'''
import sys
from base_interface import BaseAlg

class MergeSort(BaseAlg):
    ''' Implementation of merge sort
    Thomas H. Cormen Algorithms Unlocked (2013) page 54
    '''
    @staticmethod
    def merge(array, start, middle, end):
        '''Merge of two pre sorted arrays left and right
        both arrays should be have common border

        :Parameters:
        array: *list* - array of elements to sort
        start: *number* - start index of left array
        middle: *number* - end of left array end;
        end: *number* - end right array
        '''
        left = array[start:middle]
        right = array[middle:end]
        # add infinity element to the end
        left.append(sys.maxsize)
        right.append(sys.maxsize)
        left_inx = 0
        right_inx = 0
        for inx in range(start, end):
            if left[left_inx] <= right[right_inx]:
                array[inx] = left[left_inx]
                left_inx += 1
            else:
                array[inx] = right[right_inx]
                right_inx += 1


    def merge_sort(self, array, start, end, level=0):
        '''implementation of merge sort.
        It recursively split array on left and right parts
        only one element stay in sub array

        :Parameters:
        array: *list* - array of elements to sort
        start: *number* - start index of left array
        end: *number* - end right array
        '''
        if start+1 >= end:
            if self.verbosity:
                print('end loop after {} iteration'.format(level-1))
            return
        middle = int((start+end)/2)
        self.merge_sort(array, start, middle, level+1)
        self.merge_sort(array, middle, end, level+1)
        self.merge(array, start, middle, end)

    def main(self, _array):
        '''main entry point'''
        self.merge_sort(_array, 0, len(_array))
        if self.verbosity:
            print('------------------------------------------')
            print(_array)

runner = MergeSort()
runner.run()
