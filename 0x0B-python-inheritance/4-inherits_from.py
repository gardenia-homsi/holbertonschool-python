#!/usr/bin/python3
"""contain inherits_form function"""


def inherits_from(obj, a_class):
    """return if the obj is subclass of a_class"""
    if isinstance(obj, a_class) and issubclass(a_class, type(obj)):
        return False
    else:
        return True
