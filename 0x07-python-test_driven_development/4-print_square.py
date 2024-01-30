#!/usr/bin/python3
"""
print_square module
This function prints a square using '#'
"""


def print_square(size):
    """
    Return n number of '#'
    Args:
        size (int)
    """
    if isinstance(size, int) is False:
        raise TypeError("size must an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print('#', end="") for j in range(size)]
        print("")
