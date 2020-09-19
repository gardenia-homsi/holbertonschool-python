#!/usr/bin/python3
"""This module does one class that has one private integer attribute with 2 exc
eptions."""


def print_square(size):
    """this function is for printing square"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) = int and size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        rasie TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("")
