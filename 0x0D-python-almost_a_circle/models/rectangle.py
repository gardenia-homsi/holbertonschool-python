#!/usr/bin/python3
""" this model contain Rectangle class """


class Rectangle(Base):
    """this calss contain one __init__ function with 4 private atribut"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """this function define 4 private attribute and one public defiened by s
        uper class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
