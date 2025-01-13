#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Math Power Calculator
----------------------------------------------
This module takes two numbers from the user:
1. The base number
2. The power (exponent) number

It calculates the result of raising the base number to the power of the exponent using the `**` operator.

Example:
    Input:
        Base: 5
        Exponent: 3
    Output:
        Result: 125

Created on: 01/12/2025
Author: Deni Guchiev        
"""

# Step 1: Prompt the user to enter the base and power numbers
base_num = int(input("Give me the base number: "))
power_num = int(input("Give me the power number: "))

# Step 2: Calculate the power using the ** operator
result = base_num ** power_num

# Step 3: Display the result
print("Your result is:", result)
