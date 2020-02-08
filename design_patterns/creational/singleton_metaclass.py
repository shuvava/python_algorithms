#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
from threading import Lock
from typing import Optional


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instance: Optional[Singleton] = None

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Singleton(metaclass=SingletonMeta):
    value: str = None
    """
    We'll use this property to prove that our Singleton really works.
    """

    def __init__(self, value: str) -> None:
        self.value = value


def test_singleton():
    s1 = Singleton("test1")
    print(f"Object created {s1} id={id(s1)} val={s1.value}")
    s2 = Singleton("test2")
    print(f"Object created {s2} id={id(s2)} val={s2.value}")
    if id(s1) == id(s2):
        print("Same")
    else:
        print("Different")


if __name__ == "__main__":
    test_singleton()
