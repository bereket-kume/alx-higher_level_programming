#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = matrix.copy()

    def add(n):
        return n ** 2

    value = [
            list(map(lambda i: list(map(add, i)), new_matrix))
           ]
    return value
