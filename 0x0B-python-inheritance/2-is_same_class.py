#!/usr/bin/python3
"""contain is_same_class function"""


def is_same_class(obj, a_class):
    """function that check class and object"""
    if isinstance(a_class, object):
        return True
    else:
        return False
