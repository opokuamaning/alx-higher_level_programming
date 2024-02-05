#!/usr/bin/python3
"""
Module 0-lookup

A method that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """return a list of object attribute and methods"""
    return dir(obj)
