#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

----------------------------------------------
This module takes two numbers from the user:
1. The base number
2. The exponent number

It calculates the result of raising the base number to the power of the exponent using Python's built-in `pow()` function.


Example:
    Input:
        Base: 5
        Exponent: 3
    Output:
        Result: 125

Created on 01/12/2025

@author: Deni Guchiev        
"""

# Step 1: Get input from the user
base_num = float(input("Enter the base number: "))
exponent_num = float(input("Enter the exponent number: "))

# Step 2: Calculate the power using pow()
result = pow(base_num, exponent_num)

# Step 3: Display the result
print(f"The result of {base_num} raised to the power of {exponent_num} is: {result}")
