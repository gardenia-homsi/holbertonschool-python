#!/usr/bin/python3
"""contain print_sorted function"""


class MyList(list):
    """Mylist class"""
    def print_sorted(self):
        """print list in ascending order"""
        print(sorted(self))
