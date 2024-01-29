#!/usr/bin/python3
"""
Python script that adds to numbers
"""


def add_integer(a, b=98):
    """
    A funtion that returns a + b as integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
