#!/usr/bin/python
"""test rectangle model"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """test class""" 
    def test_isinstance(self):
        """test same object"""
        r1 = Rectangle(10, 2)
        self.assertEqual(isinstance(r1, Rectangle), True)

    def test_no_arg(self):
        """pass no arg"""
        r0 = Rectangle()

    def test_one_arg(self):
        """pass one argument"""
        r2 = Rectangle(10)

    def test_3_args(self):
        """pass 3 arguments"""
        r3 = Rectangle(10, 2, 3)

    def test_00_integer(self):
        """test width is integer"""
        r4 = Rectangle(2.3, 4)

    def test_01_integer(self):
        """test height is integer"""
        r5 = Rectangle(4, 2.4)

    def test_area(self):
        """test area"""
        r6 = Rectangle(10, 2)
        self.assertEqual(r6.area, 20)

    def test_str_rep(self):
        """test __str__ function"""
        r7 = Rectangle(4, 6, 2, 1, 12)
        self.asserEqual(print(r1), "[Rectangle] (12) 2/1 - 4/6")
