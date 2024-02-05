#!/usr/bin/python3
"""
A method that inherits from a list; has a public instance
method to print sorted
"""


class MyList(list):
    """
    methods:
        print_sorted(self)
    """
    def print_sorted(self):
        print(sorted(self))
