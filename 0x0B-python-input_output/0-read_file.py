#!/usr/bin/python3
"""
Contains a funtion that reads and prints content in a file
"""


def read_file(filename=""):
    """
    Read and print text froma file
    """
    with open(filename, encoding='UTF-8') as f:
        print(f.read(), end="")
