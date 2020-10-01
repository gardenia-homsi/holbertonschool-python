#!/usr/bin/python3
""" convert from json str to object"""


import json


def from_json_string(my_str):
    """ Returns an object python
        it could also be said that it converts from JSON to python
    """
    return json.loads(my_str)
