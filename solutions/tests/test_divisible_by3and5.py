#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from solutions.divisible_by_3and5 import divisible_by_3and5 

class TestDivisibleBy3And5(unittest.TestCase):
    def test_positive_case(self):
        """Test with a positive number."""
        self.assertEqual(divisible_by_3and5(20), [0, 15])
        self.assertEqual(divisible_by_3and5(50), [0, 15, 30, 45])

    def test_zero_case(self):
        """Test when the input is 0."""
        self.assertEqual(divisible_by_3and5(0), [])

    def test_small_number(self):
        """Test with a small input number."""
        self.assertEqual(divisible_by_3and5(3), [0])

    def test_large_number(self):
        """Test with a larger input number."""
        self.assertEqual(divisible_by_3and5(100), [0, 15, 30, 45, 60, 75, 90])

    def test_invalid_input(self):
        """Test invalid input cases (negative numbers or non-integer)."""
        with self.assertRaises(TypeError):
            divisible_by_3and5(-10)
        with self.assertRaises(TypeError):
            divisible_by_3and5("20")
        with self.assertRaises(TypeError):
            divisible_by_3and5(None)

if __name__ == '__main__':
    unittest.main()
