#!/usr/bin/python3
"""
Aritmethic addition of two numbers
"""


def add_integer(a, b=98):
    """
    Aritmethic addition of two numbers (integers or floats)
    returns a + b
    """    
    if (type(a) == float):
        a = int(a)
    elif (type(a) != int):
        raise TypeError("a must be an integer")
    if (type(b) == float):
        b = int(b)
    elif (type(b) != int):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
