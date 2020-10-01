#!/usr/bin/python3
"""count line number"""


def number_of_lines(filename=""):
    """return line number of file"""
    with open(filename, "r") as reader:
        for line in (filename):
            count += 1
return count
