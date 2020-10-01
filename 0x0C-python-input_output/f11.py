#!/usr/bin/python3
"""Function that returns a dictionary description"""


def class_to_json(obj):
    """from class to dict representation"""
    return obj.__dict__
