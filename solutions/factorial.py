#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# factorial.py
# Author: Jha-mal
"""
Module: factorial

A function to compute the factorial of a non-negative integer.

This file:
- Provides the 'factorial' function.
- Does not call 'factorial' directly.

Strategy:
- Uses a simple for loop from 1 to n to multiply into 'result'.
- Defensive assertion: n must be >= 0.

Implementation:
- Minimal lines of code.
- Snake_case for variables.
- Clear docstring for function.

Doctests:
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(3)
    6
"""


def factorial(n: int) -> int:
    """
    Return the factorial of a non-negative integer.

    Behavior:
      - Computes n! for any n >= 0 using an iterative approach.

    Arguments:
      :param n: int
        A non-negative integer (0, 1, 2, 3, ...).

    Return Value:
      :return: int
        The factorial of n.

    Raises:
      ValueError:
        If n is negative (factorial is undefined for negatives).

    :examples:
      >>> factorial(0)
      1
      >>> factorial(2)
      2
      >>> factorial(4)
      24
    """

    # Defensive assertion: check only "n >= 0"
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
