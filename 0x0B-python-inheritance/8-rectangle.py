#!/usr/bin/python3
"""class Rectangle"""


class Rectangle(BaseGeometry):
    """inherete from BaseGeometry"""
    def __init__(self, width, height):
        """define width and height"""
        self.__width = width
        self.__height = height
        super.integer_validator(width, self.__width)
        super.integer_validator(width, self.__width)
