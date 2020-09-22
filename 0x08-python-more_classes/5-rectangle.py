#!/usr/bin/python3
class Rectangle:
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
        str = ""
        if self.__width != 0 or self.__height != 0:
            for i in range(self.__height):
                str += "#" * self.__width
                if i < (self.__height - 1):
                    str += "\n"
        return str

    def __repr__(self):
        return("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")