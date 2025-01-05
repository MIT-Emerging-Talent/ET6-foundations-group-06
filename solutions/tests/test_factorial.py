#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# test_factorial.py
# Author: Jha-mal
"""
Module: test_factorial

Unit tests for the 'factorial' function.
"""

import unittest

from ..factorial import factorial


class TestFactorial(unittest.TestCase):
    """
    TestFactorial provides unit tests for factorial.
    """

    def test_factorial_zero(self):
        """
        Test factorial of zero is 1.
        """
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        """
        Test factorial of one is 1.
        """
        self.assertEqual(factorial(1), 1)

    def test_factorial_positive(self):
        """
        Test factorial of a typical positive integer.
        """
        self.assertEqual(factorial(5), 120)

    def test_defensive_check_negative(self):
        """
        Test that a ValueError is raised for negative integers.
        """
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()
