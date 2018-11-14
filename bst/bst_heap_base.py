'''
Implementation of a priority queue (BST) - HEAP
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec04.pdf
An array, visualized as a nearly complete binary tree 
Definition:
    root of tree: first element in the array, corresponding to i = 1 (0 index of array)
    parent(i) =i/2: returns index of node's parent
    left(i)=2i: returns index of node's left child
    right(i)=2i+1: returns index of node's right child

Max Heap Property: The key of a node is >= than the keys of its children
(Min Heap defined analogously)
'''
import abc

class BaseHeap(metaclass=abc.ABCMeta):
    '''Abstract implementation of heap class
    '''

    def __init__(self, _array=None):
        self.__array = _array or []

    @property
    def array(self):
        return self.__array

    @array.setter
    def set_array(self, array_):
        '''initialize array as a heap

        :param array_: array of elements
        :type array_: list
        '''
        if array_ is None or not isinstance(array_, list):
            return
        self.__array = array_

    @property
    def root(self):
        return self.__array[0]

    def root_index(self):
        return 0

    @property
    def length(self):
        '''Length of heap
        '''
        return len(self.array)

    def get_value(self, index):
        if index is None:
            return None
        if index < self.root_index():
            return None
        if index > self.length - 1:
            return None
        _val = self.array[index]
        if isinstance(_val, int):
            return _val
        if isinstance(_val, dict) and 'value' in _val:
            return _val['value']
        return None

    def left(self, index, max_index = None):
        '''left(i)=2(i+1): returns index of node's left child

        :param index: index of element
        :type index: Number

        :param max_index: max index value
        :type max_index: Number
        '''
        if index < self.root_index():
            return None
        if max_index is None:
            max_index =  self.length
        left = 2*(index) + 1
        if left < max_index:
            return left
        return None

    def right(self, index, max_index = None):
        '''right(i)=2i: returns index of node's right child

        :param index: index of element
        :type index: Number

        :param max_index: max index value
        :type max_index: Number
        '''
        if index < self.root_index():
            return None
        if max_index is None:
            max_index = self.length
        right = 2*(index + 1)
        if right < max_index:
            return right
        return None

    def parent(self, index):
        '''parent(i) =i/2: returns index of node's parent
        '''
        if index <= self.root_index():
            return None
        if index % 2:
            return index // 2
        return int(index/2) - 1

    def pop(self):
        '''removes the top(root) element of heap, heapify the heap and returns removed element
        '''
        self.swap(self.root_index(), self.length - 1)
        root = self.array.pop()
        self.heapify(self.root_index())
        return root

    def update(self, index, value):
        '''Updates element by index in self.array on value
        '''
        if index > len(self.array)-1:
            return
        _val = self.array[index]
        self.array[index] = value
        self.heapify(index)
        parent = self.parent(index)
        while parent is not None:
            self.heapify(parent)
            parent = self.parent(parent)

    def push(self, val):
        ''' Add a new value into self.array
        '''
        self.array.insert(self.root_index(), val)
        self.heapify(self.root_index())

    def get_sorted(self):
        '''return sorted array from heap
        '''
        _arr_sorted = []
        for i in range(self.length):
            _arr_sorted.append(self.pop())
        return _arr_sorted

    def swap(self, i, j):
        '''this method was intensionally made separate to evaluate count of calls'''
        self.__array[i], self.__array[j] = self.__array[j], self.__array[i]

    @abc.abstractmethod
    def heapify(self, index=None, max_index = None):
        '''correct a single violation of the heap property in a subtree at its root
        :Heap Property: *The key of a node is >= than the keys of its children*

        :param index: index of element (*default None == Root element of heap*)
        :type index: Number
        '''
        raise NotImplementedError('algorithm should be implemented')

    def build_heap(self):
        '''Converts A[1…n] to a max heap
        Why start at n/2? Because elements A[n/2 + 1 … n] are 
        all leaves of the tree 2i > n, for i > n/2 + 1
        Observe however that Max_Heapify takes O(1) for
        time for nodes that are one level above the leaves, and
        in general, O(l) for the nodes that are l levels above the
        leaves. We have n/4 nodes with level 1, n/8 with level 2,
        and so on till we have one root node that is lg n levels
        above the leaves.
        '''
        for index in range(int(self.length/2), -1, -1):
            self.heapify(index)
