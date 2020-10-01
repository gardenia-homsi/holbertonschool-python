#!/usr/bin/python3
"""fron jason to object"""


import json


def load_from_json_file(filename):
    """function fom json to object"""
    with open(filename, "r") as reader:
        return json.load(reader)
