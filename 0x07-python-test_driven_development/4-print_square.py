#!/usr/bin/python3
"""This module does one class that has one private integer attribute with 2 exc
eptions."""


def print_square(size):
    """this function is for printing square"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
        print("")
