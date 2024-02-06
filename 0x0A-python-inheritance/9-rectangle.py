#!/usr/bin/python3
"""
Module 6-base_geometry

Contains empty class BaseGeometry
with public instance method area and integer_validator

Contains sub class Rectagle
with attributes widht and height, validate by parents
extends parents area method and prints with __str__
"""


class BaseGeometry:
    """
    Methods:
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        """
        return: not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates input
        Args:
            name (str): string
            value (int): greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s}  must be greater than 0".format(name))

        def __init__(self, width, height):
            """
            validate and initialize widht and height
            Args:
                width (int): private
                height (int): private
            """
            super().integer_validator("width", width)
            self.width = width
            super().integer_validator("height", height)
            self.height = height
