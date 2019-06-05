#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inheirts from Rectangle.
    """

    def __init__(self, size):
        """
        Constructor method
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
