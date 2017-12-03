#add parent directory with base module
import os
from sys import path

path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../common')))

import abc
from common_interface import CommonInterface

class BaseBst(CommonInterface, metaclass=abc.ABCMeta):

    def get_data(self):
        _filename = ''
        if self.context.file is not None:
            _filename = self.context.file.strip()
        if self.context.length > 0:
            self.bst = BST.generate(self.context.length, 10 * self.context.length)
            if _filename:
                _data = self.bst.to_list()
                self._save_file(_filename, _data)
        else:
            if not _filename:
                self.bst = BST.generate(DEFAULT_LENGTH, 10 * DEFAULT_LENGTH)
            else:
                _data = self._read_file(_filename)[0]
                self.bst = BST.from_list(_data)
        if self.verbosity:
            _data = self.bst.to_list()
            print(_data)