#!/usr/bin/python3
"""count line number"""


def number_of_lines(filename=""):
    """return line number of file"""
    count = 0
    with open(filename, "r") as reader:
        for line in (reader):
            count += 1
    return count
