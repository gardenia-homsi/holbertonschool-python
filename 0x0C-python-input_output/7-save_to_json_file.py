#!/usr/bin/python3
"""to json and write in a file"""


import json


def save_to_json_file(my_obj, filename):
    """ Returns an object python
        it could also be said that it converts from JSON to python
    """
    with open(filename, "w") as writer:
        writer.write(json.dumps(my_obj))
