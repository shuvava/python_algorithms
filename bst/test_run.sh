#!/bin/bash
echo $PWD/bst
python -m unittest discover -s ./bst -p 'test_*.py'