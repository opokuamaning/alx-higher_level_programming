#!/usr/bin/python3
"""
Module 6-base_geometry

Contains empty class BaseGeometryi
with public instance method area and integer_validator
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
