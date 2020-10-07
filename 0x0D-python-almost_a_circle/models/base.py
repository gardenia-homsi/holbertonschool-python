#!/usr/bin/python3
"""This class will be the “base” of all other classes in this project"""


class Base:
    """contain 1 private '__nb_objects' and 1 public 'id' attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """check id and assign a value for it base on condition"""
        if id not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects 
