#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

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

    def __lt__(self, another_sq):
        return self.area() < another_sq.area()

    def __le__(self, another_sq):
        return self.area() <= another_sq.area()

    def __eq__(self, another_sq):
        return self.area() == another_sq.area()

    def __ne__(self, another_sq):
        return self.area() != another_sq.area()

    def __ge__(self, another_sq):
        return self.area() >= another_sq.area()

    def __gt__(self, another_sq):
        return self.area() > another_sq.area()
