#!/usr/bin/python3
"""9-base_geometry.py"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        """initate size"""
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area"""
        return self.__size * self.__size

    def __str__(self):
        """string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
