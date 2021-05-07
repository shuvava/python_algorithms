#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://habr.com/ru/post/474278/
usage
```py
class Math(object):
    @property
    def exception_handlers(self):
        return {
            ZeroDivisionError: lambda e: 'division on zero is forbidden'
        }

    @ProcessException(exception_handlers)
    def divide(self, a, b):
        return a // b
```
"""

from asyncio import QueueEmpty, QueueFull
from concurrent.futures import TimeoutError
from inspect import iscoroutinefunction


class ProcessException(object):

    __slots__ = ('handlers',)

    def __init__(self, custom_handlers=None):
        if isinstance(custom_handlers, property):
            custom_handlers = custom_handlers.__get__(self, self.__class__)

        raise_exception = ProcessException.raise_exception

        exclude = {
            QueueEmpty: lambda e: None,
            QueueFull: lambda e: None,
            TimeoutError: lambda e: None
        }

        self.handlers = {
            **exclude,
            **(custom_handlers or {}),
            Exception: raise_exception
        }

    def __call__(self, func):
        handlers = self.handlers

        if iscoroutinefunction(func):
            async def wrapper(*args, **kwargs):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    return handlers.get(e.__class__, handlers[Exception])(e)
        else:
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    return handlers.get(e.__class__, handlers[Exception])(e)

        return wrapper

    @staticmethod
    def raise_exception(e: Exception):
        raise e
