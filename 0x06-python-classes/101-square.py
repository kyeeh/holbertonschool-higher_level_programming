#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        sq_str = ""
        if (self.size == 0):
            print()
        else:
            sq_str += "\n" * self.position[1]
            for i in range(0, self.size):
                sq_str += (" " * self.position[0]) + ("#" * self.size)
                if i < self.size - 1: 
                    sq_str += "\n"
            return (sq_str)

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if (self.size == 0):
            print()
        else:
            for i in range(0, self.position[1]):
                print()
            for i in range(0, self.size):
                print((" " * self.position[0]) + ("#" * self.size))

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (type(value) != tuple) or (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) != int) or (type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
