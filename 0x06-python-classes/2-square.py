#!/usr/bin/python3
"""This module does one class that has one private integer attribute with 2 exc
eptions."""


class Square:
    """This class does one private attribute."""
    try:
        def __init__(self, size=0):
            self.__size = size
    if type(x) != <type 'int'>:
        except TypeError:
            print("size must be an integer")
    if size < 0:
        except ValueError:
            print("size must be >= 0")
