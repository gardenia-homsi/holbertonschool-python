#!/usr/bin/python3
"""append string to txt file"""


def append_write(filename="", text=""):
    """ Append content to a file, it doesn´t exist then is created """
    with open(filename, "a", encoding="utf-8") as writer:
        return writer.write(text)
