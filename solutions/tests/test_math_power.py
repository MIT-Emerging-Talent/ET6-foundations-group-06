#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit tests for the Math Power program.

"""

import unittest
from math import pow


class TestMathPower(unittest.TestCase):
    """Test suite for the Math Power program."""

    def test_positive_integers(self):
        """Test power calculation with positive integers."""
        self.assertAlmostEqual(pow(2, 3), 8.0)
        self.assertAlmostEqual(pow(5, 4), 625.0)

    def test_positive_floats(self):
        """Test power calculation with positive floats."""
        self.assertAlmostEqual(pow(2.5, 3), 15.625)
        self.assertAlmostEqual(pow(1.1, 2.5), 1.331)

    def test_negative_base(self):
        """Test power calculation with a negative base."""
        self.assertAlmostEqual(pow(-2, 3), -8.0)
        self.assertAlmostEqual(pow(-2, 2), 4.0)

    def test_negative_exponent(self):
        """Test power calculation with a negative exponent."""
        self.assertAlmostEqual(pow(2, -3), 0.125)
        self.assertAlmostEqual(pow(10, -2), 0.01)

    def test_zero_cases(self):
        """Test power calculation with zero as base or exponent."""
        self.assertAlmostEqual(pow(0, 5), 0.0)
        self.assertAlmostEqual(pow(5, 0), 1.0)
        self.assertAlmostEqual(pow(0, 0), 1.0)  # Conventionally defined as 1


if __name__ == "__main__":
    unittest.main()
