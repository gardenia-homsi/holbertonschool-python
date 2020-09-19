#!/usr/bin/python3
"""kamal"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        with self.assertRaises(KeyError):
            max_integer({'a': 1, 'b': 2})
        self.assertEqual(max_integer([1, float('inf'), 4, 10]), float('inf'))

        self.assertEqual(max_integer([1, 2, 3, 5]), 5)
        self.assertEqual(max_integer(), None)

        self.assertEqual(max_integer([]), None)

        self.assertEqual(max_integer("abcdefghijklmnopqrstuvwxyz"), 'z')

        self.assertEqual(max_integer(" "), ' ')

        self.assertEqual(max_integer([[]]), [])

        with self.assertRaises(TypeError):
            max_integer(67)

        self.assertEqual(max_integer([0, -2, -30]), 0)
