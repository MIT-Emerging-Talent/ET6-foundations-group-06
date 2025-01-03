# sum_list.py
# Author: Jha-mal
"""
Module: sum_list

A function that sums all numbers in a list.
"""

from typing import List


def sum_list(numbers: List[float]) -> float:
    """
    Return the sum of all numbers in the list.

    :param numbers: A list of numeric values.
    :return: Sum of the numbers.

    >>> sum_list([1, 2, 3])
    6
    >>> sum_list([])
    0
    >>> sum_list([-1, 1, 5.5])
    5.5
    """
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError("All items must be numeric.")
    return sum(numbers)
