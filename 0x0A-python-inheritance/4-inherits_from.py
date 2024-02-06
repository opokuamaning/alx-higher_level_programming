#!/usr/bin/python3
"""
Module 4-inherits_from.py

Returns True if object is exactly an instance of
class it inherited from or is subcls of"
"""


def inherits_from(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use isinstance() to get a class and parent class
        use issubclass(0 to get what object is subclass of

    Return:
        True if obj is exactly an instace of class that it inherited from
        or is subclass of
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
