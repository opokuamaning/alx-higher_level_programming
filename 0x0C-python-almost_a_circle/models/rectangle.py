#!/usr/bin/python3
"""
Module: Rectangle class
Inherits base class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    @property
    def width(self):
        """width function private"""

        return self.__width

    @width.setter
    def width(self, value):
        """width function for setter"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height function private"""

        return self.__height

    @height.setter
    def height(self, value):
        """height function private"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x function private"""

        return self.__x

    @x.setter
    def x(self, value):
        """x function setter"""

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y function private"""

        return self.__y

    @y.setter
    def y(self, value):
        """y function setter"""

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
