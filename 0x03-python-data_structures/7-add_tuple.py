#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = validate_tuple(tuple_a)
    tuple_b = validate_tuple(tuple_b)
    return ((tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]))


def validate_tuple(tup=()):
    size = len(tup)
    if (size == 0):
        return ((0, 0))
    if (size == 1):
        tup = list(tup)
        tup.append(0)
        tup = tuple(tup)
    return (tup)
