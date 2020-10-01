#!/urs/bin/python3
"""read line"""


def read_lines(filename="", nb_lines=0):
    """function that read nb of line from a file"""
    with open(filename, "r") as reader:
        if nb_lines <= 0 or nb_lines >= len(open(filename).readlines()):
            for line in reader:
                print(line, end="")
        else:
            for i in range(0, nb_lines):
                print(reader.readline(), end="")
