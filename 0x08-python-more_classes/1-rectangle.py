#!/usr/bin/python3
"""
A ractangle class with private attributes width and height
"""


class Rectangle:
    """
    A rectangle class with private attributes width and and height

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width,height)
        width(self)
        height(self)
        width(self, value)
        height(self, value)
    """
    def __init__(self, width=0, height=0):
        """Initialize rectangles"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets width if width > 0"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting returns og height"""
        return self.height

    @height.setter
    def height(self, value):
        """This sets height if it is > 0"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
