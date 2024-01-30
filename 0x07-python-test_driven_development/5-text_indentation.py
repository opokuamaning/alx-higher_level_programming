#!/usr/bin/python3
"""
Module 5-text_indentation
A method that prints with 2 new lines after each ",", "?", and ":"
"""


def text_indentation(text):
    """
    prints with 2 new lines after each ",", "?", and ":"
    Args:
        text (str)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = '\n'.join(list_lines)
    print(revised, end="")
