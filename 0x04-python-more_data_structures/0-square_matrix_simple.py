#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same input size
    new_matrix = [[0 for _ in row] for row in matrix]

    # iterate over the rows and cols of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Compute rhe square of each matrix
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
