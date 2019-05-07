#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        size = len(arr)
        for i, n in enumerate(arr):
            if (i < size - 1):
                print("{:d} ".format(n), end='')
            else:
                print("{:d}".format(n), end='')
        print("")
