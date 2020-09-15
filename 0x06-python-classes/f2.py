#!/usr/bin/python3
"""This module does one class that has one private integer attribute with 2 exceptions."""


class Square:
    """This class does one private attribute."""
    try:
        def __init__(self, size=0):
            self.__size = size
    exception TypeError:
        if type(size) == integer:
            print("size must be an integer")
    exception ValueError:
        if size < 0:
            print("size must be >= 0")
