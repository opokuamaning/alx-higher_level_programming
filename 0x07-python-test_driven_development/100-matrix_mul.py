#!/usr/bin/python3
"""
Matrix_mul module
Function that multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """
    Return a matrix with the product of m_a and m_b
    Args:
        m_a (list of list)
        m_b (list of list)
    Raise: TypeError, ValueError
    """
    if isinstance(m_a, list) is False:
        raise TypeError("m_a must be a list")
    if isinstance(m_b, list) is False:
        raise TypeError("m_b must be a list")
    for item in m_a:
        if isinstance(item, list) is False:
            raise TypeError("m_a must be a list of lists")
    for item in m_b:
        if isinstance(item, list) is False:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for rows in m_a:
        for cols in rows:
            if not type(cols) in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for rows in m_b:
        for cols in rows:
            if not type(cols) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    mat_len = 0

    for items in m_a:
        if mat_len != 0 and mat_len != len(items):
            raise TypeError("each row of m_a must be of the same size")
        mat_len = len(items)

    mat_len = 0
    for items in m_b:
        if mat_len != 0 and mat_len != len(items):
            raise TypeError("each row of m_b must be of the same size")
        mat_len = len(items)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    reverse_matrix = []
    for i in range(len(m_b[0])):
        new_row = []
        for j in range(len(m_b)):
            new_row.append(m_b[j][i])
        reverse_matrix.append(new_row)

    new_mat = []
    for irow in m_a:
        new_row = []
        for jcol in reverse_matrix:
            value = 0
            for k in range(len(reverse_matrix[0])):
                value += irow[k] * jcol[k]
            new_row.append(value)
        new_mat.append(new_row)

    return (new_mat)
