#!/usr/bin/env python3
# encoding: utf-8
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2017-2022 Vladimir Shurygin. All rights reserved.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''Singletone pattern
we override the __new__ method
(Python's special method to instantiate objects) to control the object creation.
The s object gets created with the __new__ method, but before this,
it checks whether the object already exists. The hasattr method
(Python's special method to know if an object has a certain property)
is used to see if the cls object has the instance property,
which checks whether the class already has an object.

:Module-level Singletons:

All modules are Singletons by default because of Python's importing behavior. 
Python works in the following way:
1. Checks whether a Python module has been imported.
2. If imported, returns the object for the module. If not imported, 
    imports and instantiates it.
3. So when a module gets imported, it is initialized.
    However, when the same module is imported again,
    it's not initialized again, which relates to the Singleton behavior
    of having only one object and returning the same object.
'''


class Singleton(object):
    '''Singletone python realization'''

    def __new__(cls, *args, **kwargs):
        '''Object initialization
        The hasattr method (Python's special method to know if an object has
        a certain property) is used to see if the cls object has the instance
        property, which checks whether the class already has an object.
        '''
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.instance


def test_singleton():
    s1 = Singleton()
    print(f"Object created {s1} id={id(s1)}")
    s2 = Singleton()
    print(f"Object created {s2} id={id(s2)}")
    if id(s1) == id(s2):
        print("Same")
    else:
        print("Different")


if __name__ == "__main__":
    test_singleton()
