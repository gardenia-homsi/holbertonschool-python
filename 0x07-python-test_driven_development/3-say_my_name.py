#!/usr/bin/python3
"""this module has function to print fist name and last name"""


def say_my_name(first_name, last_name=""):
    """this function take 2 string parameter and return last name and first nam
    e"""
    if type(fist_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(fist_name, last_name))
