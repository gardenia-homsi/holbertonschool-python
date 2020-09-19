#!/usr/bin/python3
"""this module is to bprint string with conditions"""


def text_indentation(text):
    """Write a function that prints a text with 2 new lines after each of these
    characters: ., ?"""
    if type(text) is str:
        copy-str = text
        for c in copy-str:
            if c is '.' or c is '?' or c is ':':
                copy-str.replace(c+1, '')             
        for s in copy-str:
            if s is '.' or s is '?' or s is ':':
                print("\n")
            else:
                print(s, end="")
    else:
        raise TypeError("text must be a string")
