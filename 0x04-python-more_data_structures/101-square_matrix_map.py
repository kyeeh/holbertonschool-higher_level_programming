#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return ([list(map((lambda x: x ** 2), arr)) for arr in matrix])
