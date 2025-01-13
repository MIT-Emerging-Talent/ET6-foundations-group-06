#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit tests for the Celsius to Fahrenheit conversion function.

"""

import unittest
from solutions.celsius_to_fahrenheit import celsius_to_fahrenheit


class TestCelsiusToFahrenheit(unittest.TestCase):
    """Test suite for the Celsius to Fahrenheit conversion function."""

    def test_positive_temperature(self):
        """Test conversion for positive Celsius temperatures."""
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0, places=2)
        self.assertAlmostEqual(celsius_to_fahrenheit(25), 77.0, places=2)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212.0, places=2)

    def test_negative_temperature(self):
        """Test conversion for negative Celsius temperatures."""
        self.assertAlmostEqual(celsius_to_fahrenheit(-10), 14.0, places=2)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40.0, places=2)

    def test_zero_temperature(self):
        """Test conversion for zero Celsius."""
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0, places=2)

    def test_float_temperature(self):
        """Test conversion for float (decimal) Celsius temperatures."""
        self.assertAlmostEqual(celsius_to_fahrenheit(36.6), 97.88, places=2)
        self.assertAlmostEqual(celsius_to_fahrenheit(-18.5), -1.3, places=2)


if __name__ == "__main__":
    # Run the tests when the script is executed directly
    unittest.main()
