#!/usr/bin/python3
"""
Contains function that appends to a text file and returns number
of charachters added
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
