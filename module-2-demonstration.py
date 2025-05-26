"""
Description: Module 2 demonstration
Author: Ivan Estropigan
Date: May 23, 2025
Usage: To demonstrate content from module 2.
"""
name = "Ivam"
age = 24
value = 3.14159
number = 123
absolute_value = abs(-12)
current_salary = 67293.21
is_employed = True
PI = 3.14159 
Federal_TAX_RATE = 0.05
# Functions
print('absolute value:', absolute_value)

# Function embedded within another function.
print('absolute value:', abs(-12))


# Print with f strings 
print(f"My name is {name} and I am {age} years old.")
# Outputs my name and age.

print(f"The value of pi is {value:.2f}.")
# Outputs the value of Pi

print(f"The number is {number:05}.")
# Outputs the number is 00123

print(f"Hello, {name:>10}.")
# Hello,          Ivan

# Simple Data Type 
print(type(name))
print(type(age))
print(type(current_salary))
print(type(is_employed))

# Type Conversions
age_and_salary = age + current_salary # implicit

months_old = "11"
years_old = 25
age = float(years_old) + (float(months_old / 12)) # explicit

print("Age as a float:", age) # outputs age as a float: 25.916^

age = int(age) # explicit
print("Age as an int:", age) # outputs Age as an int: 25


