#!/usr/bin/python3
"""contain inherits_form function"""


def inherits_from(obj, a_class):
    """return if the obj is subclass of a_class"""
    if issubclass(obj, a_class):
        return True
    else:
        return False
