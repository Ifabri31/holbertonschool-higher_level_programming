#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            end = ' '
            if i is row[-1]:
                end = ''
            print("{:d}".format(i), end=end)
        print()
