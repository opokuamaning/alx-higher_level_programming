#!/usr/bin/python3
"""
Defines a Base class

Contains private class __nb_objects and class sonstructor __init__
"""


class Base():
    """
    defines base class
    Attributes:
        __nb_objects
    Methods: __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        increment __nb_objects and assign the new value to the public instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
