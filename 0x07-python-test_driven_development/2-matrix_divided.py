#!/usr/bin/python3
"""
Module 2-matrix_divided
A module that divides all element in matrix and returns new matrix
"""


def matrix_divided(matrix, div):
    """
    Returns new matrix with division
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not is_matrix_number(matrix):
        raise TypeError(message)

    if not is_matrix_row_same_size(matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for lists in matrix:
        newlist.append(round(i/div, 2))
        new_matrix.append(newlist)
    return new_matrix


def is_matrix_number(matrix):
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                return False
    return True


def is_matrix_row_same_size(matrix):
    for row in matrix:
        if len(row) != len(matrix[0]):
            return False
    return True
