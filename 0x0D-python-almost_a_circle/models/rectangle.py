#!/usr/bin/python3
""" this model contain Rectangle class """


class Rectangle(Base):
    """this calss contain one __init__ function with 4 private atribut"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """this function define 4 private attribute and one public defiened by s
        uper class"""
        __width = width
        __height = height
        __x = x
        __y = y
        id = super().id
