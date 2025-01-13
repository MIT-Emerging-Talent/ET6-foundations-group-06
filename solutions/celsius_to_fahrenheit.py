#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module to convert temperature from Celsius to Fahrenheit.

Formula:
    Fahrenheit = (Celsius * 9 / 5) + 32

Example:
    Input: 25 (Celsius)
    Output: 77.0 (Fahrenheit)

Created on 01/12/2025

@author: Deni Guchiev
"""

# Step 1: Prompt the user to enter the temperature in Celsius
# The input is converted to a floating-point number for calculations
celsius = float(input("Enter temperature in degrees Celsius: "))

# Step 2: Convert Celsius to Fahrenheit using the formula
fahrenheit = celsius * 9 / 5 + 32

# Step 3: Output the result in Fahrenheit
# Print the Fahrenheit temperature to the user
print("Temperature in Fahrenheit:", fahrenheit)
