#!/usr/bin/python3
"""This module does one class that has one private integer attribute with 2 exc
eptions."""


def print_square(size):
    """this function is for printing square"""
     if type(size) is int:
        if size >= 0:
            for iter in range(size):
                for iter2 in range(size):
                    print("#", end="")
                print("")
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
