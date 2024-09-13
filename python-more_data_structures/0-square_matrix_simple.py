#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_2 = []
    for row in matrix:
        row_2 = []
        for num in row:
            row_2.append(num ** 2)
        matrix_2.append(row_2)
    return matrix_2
