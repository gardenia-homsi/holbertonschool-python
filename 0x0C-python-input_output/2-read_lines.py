#!/usr/bin/python3
"""read based on nb lines"""


def read_lines(filename="", nb_lines=0):
    """ Read the file acording to number of required lines """
    a = 0
    with open(filename, encoding="utf-8") as reader:
        for line in reader:
            print(line, end="")
            if a == (nb_lines - 1):
                break
            a += 1
