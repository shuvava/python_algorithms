#!/usr/bin/env python3
# encoding: utf-8
x = (1, 2, 4, 8, 16)

def func_opt_arg(value, seq=None):
    if seq is None:
        seq = []
    seq.append(value)
    return seq

if __name__ == '__main__':
    print(x)
    a, b, c, d, e = x
    print(a, b, c, d, e)
    a, *y, e = x #The point is that the variable with * collects the values not assigned to others.
    print(a, e, y)
    x = 4
    print(x >= 2 and x <= 8)
    print(2 <= x <= 8)
    print(2 <= x <= 3)
    x = y = z = 2
    print(x, y, z)
    #You can apply zip and get tuples of the corresponding items
    x = [1, 2, 4, 8, 16]
    y = 'abcde'
    for item in zip(x, y):
        print(item)
    #Iterating over a dictionary yields its keys
    z = {'a': 0, 'b': 1}
    for k in z:
        print(k, z[k])
    
