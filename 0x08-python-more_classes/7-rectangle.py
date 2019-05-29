#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        me_as_str = ""
        if (not(self.__width == 0) or (self.__height == 0)):
            for i in range(0, self.__height - 1):
                me_as_str += str(self.print_symbol) * self.__width + "\n"
            me_as_str += str(self.print_symbol) * self.__width
        return me_as_str

    def __repr__(self):
        return "Rectangle({:d},{:d})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if ((self.__width == 0) or (self.__height == 0)):
            return 0
        return (self.__width * 2 + self.__height * 2)
