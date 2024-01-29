#!/usr/bin/python3
"""
A ractangle class with private attributes width and height,
and public area and perimeter methods
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
        area(self)
        perimeter(self)
    """
    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets width if int > 0 """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets height if int > 0 """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """Return 2*width + 2*height (or return 0 if width or heihgt is 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Prints a rectangle with #'s"""
        rect = ""
        if self.__width == 0 or self.height == 0:
            return rect

        for i in range(self.__height):
            rect += ("#" * self.__width) + "\n"

        return rect[:-1]
