#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    size = len(matrix)
    for arr in matrix:
        for i, n in enumerate(arr):
            if (i < size - 1):
                print("{:d} ".format(n), end = '')
            else:
                print("{:d}".format(n), end = '')
        print("")