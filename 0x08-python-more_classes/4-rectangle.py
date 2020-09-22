#!/usr/bin/python3
"""gardenia"""


class Rectangle:
    """rectangel"""
    def __init__(self, width=0, height=0):
        if type(width) is int:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        if type(height) is int:
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        return self.__width

    @setter.width
    def width(self, value):
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @setter.height
    def height(self, value):
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Redefine the method str to print the rectangle """
        s = ""
        if self.width != 0 and self.height != 0:
            for i in range(self.height):
                s += "#" * self.width
                if i < (self.height - 1):
                    s += "\n"

        return s

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)