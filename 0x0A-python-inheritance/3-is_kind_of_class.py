#!/usr/bin/python3
"""
Module 3-is_kind_of_class

Returns True if object is exactly an instance of class it inherited from"
"""


def is_kind_of_class(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use isinstance() to get a class and parent class
        use issubclass(0 to get what object is subclass of

    Return:
        True if obj is exactly an instace of class that it inherited from
    """
    return isinstance(obj, a_class)
