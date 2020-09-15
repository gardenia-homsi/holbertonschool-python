#!/usr/bin/python3
"""This module does one class that has one private integer attribute with 2 exc
eptions."""


class Square:
    """This class does one private attribute."""
    def __init__(self, size=0):
            self.__size = size
    if type(self.__size) != int:
        raise TypeError("size must be an integer")
    if self.__size < 0:
        raise ValueError("size must be >= 0")
