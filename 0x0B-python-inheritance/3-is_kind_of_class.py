#!/usr/bin/python3
"""contain is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """ Returns true if the object is exactly an instance of the a_class
        or an instance of the superclass
    """
    return isinstance(obj, a_class)
