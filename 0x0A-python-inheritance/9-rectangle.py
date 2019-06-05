#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inheirts from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Constructor method
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns Rectangle area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns Rectangle description
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
