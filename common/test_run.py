#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
# python -m unittest discover -s ./bst -p 'test_*.py'

# import glob
# import unittest
# import os

# print('{}\\test_*.py'.format(os.path.dirname(__file__)))
# test_files = glob.glob('{}\\test_*.py'.format(os.path.dirname(__file__)))
# print(test_files)
# module_strings = [test_file[0:len(test_file)-3] for test_file in test_files]
# print(module_strings)
# suites = [unittest.defaultTestLoader.loadTestsFromName(test_file) for test_file in module_strings]
# print(suites)
# test_suite = unittest.TestSuite(suites)
# test_runner = unittest.TextTestRunner().run(test_suite)