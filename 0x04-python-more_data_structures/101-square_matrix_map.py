#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = matrix.copy()

    def add(n):
        return n ** 2

    value = [
           list(map(add, i)) for i in new_matrix
           ]
    return value
