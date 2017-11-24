#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2017 Vladimir Shurygin.  All rights reserved.
#
'''
The Monostate Singleton pattern
Singleton design pattern says that there should be one and only one
object of a class. However, as per Alex Martelli, typically
what a programmer needs is to have instances sharing the same state.
He suggests that developers should be bothered about the state and
behavior rather than the identity. As the concept is based on
all objects sharing the same state, it is also known as
the Monostate pattern.
'''
class Singleton:
    '''
    The Monostate pattern can be achieved in a very simple way in Python.
    In the following code, we assign the __dict__ variable
    (a special variable of Python) with the __shared_state class variable.
    Python uses __dict__ to store the state of every object of a class.
    In the following code, we intentionally assign __shared_state to all
    the created instances. So when we create two instances, 'b' and 'b1',
    we get two different objects unlike Singleton where we have just one object.
    However, the object states, b.__dict__ and b1.__dict__ are the same.
    '''
    __shared_state = {'1': '2'}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

class SingletonAnotherImplementation:
    __shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(SingletonAnotherImplementation, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj

b = Singleton()
b1 = Singleton()
b.x = 4
print("Borg Object 'b': ", b) ## b and b1 are distinct objects
print("Borg Object 'b1': ", b1)
print("Object State 'b':", b.__dict__)## b and b1 share same state
print("Object State 'b1':", b1.__dict__)