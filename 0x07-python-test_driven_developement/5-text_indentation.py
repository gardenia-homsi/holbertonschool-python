#!/usr/bin/python3
"""this module is to bprint string with conditions"""


def text_indentation(text):
    """Write a function that prints a text with 2 new lines after each of these
    characters: ., ?"""
    for s in text:
        if s == "." or s == "?":
            print()
        else:
            print(s, end="")
