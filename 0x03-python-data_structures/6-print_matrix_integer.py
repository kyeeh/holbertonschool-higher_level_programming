#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for n in arr:
            print("{:d} ".format(n), end = '')
        print("")