#!/usr/bin/python3
"""class Rectangle"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """inherete from BaseGeometry"""
    def __init__(self, width, height):
        """define width and height"""
        super.integer_validator("width", width)
        super.integer_validator("height", height)
        self.__width = width
        self.__height = height
