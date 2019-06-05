#!/usr/bin/python3


class BaseGeometry():
    """
    BaseGeometry class.
    """

    def area(self):
        """
        Raises an Excpetion because area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value...
        if value is not an integer: raise a TypeError exception.
        if value is less or equal to 0: raise a ValueError
        """
        if (type(value) != int):
            raise TypeError(name + " must be an integer")
        if (value <= 0):
            raise ValueError(name + " must be greater than 0")
