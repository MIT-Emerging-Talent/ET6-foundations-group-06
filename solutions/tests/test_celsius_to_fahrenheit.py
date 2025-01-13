#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from solutions.celsius_to_fahrenheit import celsius_to_fahrenheit

class TestCelsiusToFahrenheit(unittest.TestCase):
    def test_positive_temperature(self):
        """Test conversion for positive Celsius temperatures."""
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(25), 77.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212.0)

    def test_negative_temperature(self):
        """Test conversion for negative Celsius temperatures."""
        self.assertAlmostEqual(celsius_to_fahrenheit(-10), 14.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_zero_temperature(self):
        """Test conversion for 0 Celsius."""
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0)

    def test_float_temperature(self):
        """Test conversion for float Celsius temperatures."""
        self.assertAlmostEqual(celsius_to_fahrenheit(36.6), 97.88)
        self.assertAlmostEqual(celsius_to_fahrenheit(-18.5), -1.3)


if __name__ == "__main__":
    unittest.main()
