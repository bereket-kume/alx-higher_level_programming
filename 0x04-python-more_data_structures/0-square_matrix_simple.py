#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for i in matrix:
        new_row = [x ** 2 for x in i]
        new_list.append(new_row)
    return new_list
