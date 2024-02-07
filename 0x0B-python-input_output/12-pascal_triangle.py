#!/usr/bin/python3
"""
returns a list of lists of integers representing the
Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Returns:
        empty list [] if n<= 0
        if n is 5, we should return
            [1]
            [1,1]
            [1,2,1]
            [1,3,3,1]
            [1,4,6,4,1]
   """

    matrix = []
    prev = []

    for i in range(n):
        res_list = []
        p1 = -1
        p2 = 0
        for j in range(len(prev) + 1):
            if p1 == -1 or p2 == len(prev):
                res_list += [1]
            else:
                res_list += [prev[p1] + prev[p2]]
            p1 += 1
            p2 += 1
        matrix.append(res_list)
        prev = res_list[:]

    return matrix
