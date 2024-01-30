#!/usr/bin/python3
"""
Module 2-matrix_divided
A module that divides all element in matrix and returns new matrix
"""


def matrix_divided(matrix, div):
    """
    Returns new matrix with division
    """
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(message)

    new_matrix = []
    samelen = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(message)
        if len(lists) != samelen:
            raise TypeError("Each row of the matrix must have the same size")
        newlist = []
        for i in lists:
            if (isinstance(i, (int, float))) is False:
                raise TypeError(message)
            newlist.append(round(i/div, 2))
        new_matrix.append(newlist)
    return new_matrix
