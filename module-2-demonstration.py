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

# SIMPLE DATA TYPE
print(type(name))
print(type(age))
print(type(current_salary))
print(type(is_employed))

# TYPE CONVERSIONS
age_and_salary = age + current_salary # implicit

months_old = "11"
years_old = 25
age = float(years_old) + (float(months_old / 12)) # explicit

print("Age as a float:", age) # outputs age as a float: 25.916^

age = int(age) # explicit
print("Age as an int:", age) # outputs Age as an int: 25

# STANDARD OPERATORS

## '=' Assignment to set the value of a variable
# Assign a value to a variable 
age = 20 
greetings = 'Hello, world!'
number_list = [1, 2, 3]

#Assign the result of an expression to a variable
sum_result = 5 + 3
concatenation_result = 'Hello' + '' + 'World'

# Assign the value of one variable to another
backup_age = age 

## '+' Addition to sum two numbers, also used with text Strings for Concatenation(combining text together)
result = 5 + 5 
# result = 10 

full_name = "John" + " " + "Doe"
#full_name = "John Doe"

## '-' Subtraction to get the difference of two numbers
result = 10 - 5 
# result = 5 

## '*' Multiplication to get the product of two numbers
result = 14 * 3 
# result = 42

## '/' Division to get the quotient of two numbers. with decimal
result = 42 / 4 
# result = 10.5

## '//' Floor Division to get the quotient of two numbers, with no decimal (aka: integer division)
result = 42 // 4 
# = 10

## '**' Exponentiation to get the result of the first number to the power of the second
result = 2 ** 4 
#result 16

# SHORTCUT OPERATORS

# '+=' Combines addition and assignment into a single operator
age += 1 
#same as:
age = age + 1

# '-=' Combines subtraction and assignment into a single operator. 
count -= 1  # type: ignore
#same as:
count = count - 1

# '/=' Combines division and assignment into a single operator.
half /= 2 # type: ignore
#same as: 
half = half / 2

# '//=/ Combines floor division and assignment into a single operator
third //=3  # type: ignore
#same as:
third = third // 3 

# '%=' Combines modulus and assignment into a single operator
remainder %= 2  # type: ignore
#same as 
remainder = remainder % 2 

# '**=' Combines exponentiation and assignment into a single operator
power **= 3 # type: ignore
#same as: 
power = power * 3

## ORDER OF OPERATIONS
result = ((10 + 5) * 2) / 3
#result = 10.0

#versus: 
result = 10 + 5 * 2 / 3 
#result = 13.33^ 