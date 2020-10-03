#!/usr/bin/python3
"""Module 2-is_same_class.py"""


def is_same_class(obj, a_class):
    """check if obj is a_class"""
    if type(obj).__name__ == a_class.__name__:
        return True
    else:
        return False
