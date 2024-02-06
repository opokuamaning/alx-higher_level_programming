#!/usr/bin/python3
"""
Module 2-is_same_class

Returns True if object is exactly an instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use isinstance() to get a class and parent class
        use issubclass(0 to get what object is subclass of

    Return:
        True if obj is exactly an instaco of specified classs
    """
    return type(obj) == a_class
