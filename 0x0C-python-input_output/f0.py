#!/usr/bin/python3
def read_file(filename=""):
    """function to read file and print output"""
    with open(filename, "r") as reader:
        for line in reader:
            print(line, end="")
