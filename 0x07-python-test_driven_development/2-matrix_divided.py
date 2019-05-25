#!/usr/bin/python3
"""
Divides all elements of a matrix with validations.
"""


def matrix_divided(matrix, div):
    """
    Matrix division by a scalar
    returns Matrix (as the movie but in reverse)
    """
    size = len(matrix[0])
    type_msg = "matrix must be a matrix (list of lists) of integers/floats)"
    size_msg = "Each row of the matrix must have the same size"
    div_msg = "div must be a number"
    div0_msg = "division by zero"
    new_matrix = []
    if (is_number(div, div_msg) and non_zero(div, div0_msg)):
        if (is_list(matrix, type_msg)):
            for row in matrix:
                if (is_list(row, type_msg) and same_size(row, size, size_msg)):
                    new_row = []
                    for e in row:
                        if (is_number(e, type_msg)):
                            new_row.append(round(e / div, 2))
                    new_matrix.append(new_row)
    return (new_matrix)


def is_number(e, msg):
    if (is_int(e, msg) or is_float(e, msg)):
        return True
    else:
        raise TypeError(msg)


def is_int(e, msg):
    return (type(e) == int)


def is_float(e, msg):
    return (type(e) == float)


def is_list(e, msg):
    if (type(e) == list):
        return True
    else:
        raise TypeError(msg)


def same_size(e, size, msg):
    if (len(e) == size):
        return True
    else:
        raise TypeError(msg)


def non_zero(e, msg):
    if (e != 0):
        return True
    else:
        raise ZeroDivisionError(msg)
