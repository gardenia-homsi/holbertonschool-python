#!/usr/bin/python3
"""write object to a file using json representation"""

import json


def save_to_json_file(my_obj, filename):
    """ function"""
    JsonRep = json.dumps(my_obj)
    with open(filename, 'w') as writer:
        writer.write(JsonRep)
