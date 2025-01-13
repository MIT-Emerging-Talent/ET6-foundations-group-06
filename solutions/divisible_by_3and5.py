#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module to find all numbers smaller than a given input number
that are divisible by both 3 and 5.

Module contents:
    - Finds numbers smaller than `num` that are divisible by 3 and 5.

Created on 01/12/2025

@author: Deni Guchiev
"""

def divisible_by_3and5(num):
    """
    Finds numbers smaller than `num` that are divisible by 3 and 5.

    Parameters:
        num (int): The upper limit to check for divisibility.

    Returns:
        list: A list of numbers divisible by 3 and 5.

    Raises:
        TypeError: If `num` is not an integer.
        ValueError: If `num` is a negative integer.
    """
    if not isinstance(num, int):
        raise TypeError("Input must be an integer.")
    if num < 0:
        raise ValueError("Input must be a non-negative integer.")

    result = []
    for i in range(num):
        if i % 3 == 0 and i % 5 == 0:
            result.append(i)
    return result


if __name__ == "__main__":
    # Usage Instructions:
    # 1. Run this script directly or import the function into another module.
    # 2. Example of running directly:
    #        $ python3 script_name.py
    #        Enter your number: 20
    #        [0, 15]
    # 3. Import the function into your Python script:
    #        from script_name import divisible_by_3and5
    # 4. Call the function with a positive integer argument:
    #        result = divisible_by_3and5(50)
    #        print(result)

    try:
        num = int(input("Enter your number: "))
        if num < 0:
            raise ValueError("Input must be a non-negative integer.")
        result = divisible_by_3and5(num)
        print(result)
    except (TypeError, ValueError) as e:
        print(f"Invalid input: {e}")
