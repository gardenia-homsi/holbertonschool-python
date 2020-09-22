#!/usr/bin/python3
"""gardenia"""


class Rectangle:
    """function that initiate rectangle"""
    def __init__(self, width=0, height=0):
        """ Initialice the values """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """print the rectangle"""
        str = ""
        if self.__width != 0 or self.__height != 0:
            for i in range(self.__height):
                str += "#" * self.__width
                if i < (self.__height - 1):
                    str += "\n"
        return str
