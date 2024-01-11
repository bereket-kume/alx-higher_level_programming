#!/usr/bin/python3
"""module for matrix_divided"""


def matrix_divided(matrix, div):
    """matrix divided method"""

    if not isinstance(matrix, list) or not all\
            (isinstance(row, list) for row in matrix) or \
            not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    rowsize = len(matrix[0])
    if not all(len(row) == rowsize for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(num/div, 2) for num in row] for row in matrix]
    return new_matrix
