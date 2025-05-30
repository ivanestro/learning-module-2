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

## PYTHON COLLECTION TYPES 

#LISTS
# A list of integers 
daily_step_count = [10343, 9385,7029,10931,5921]

# A list of mixed data values.
employee_data = ["A123", 55024.23, 595, True]

# A list of lists
lists_of_lists = [["A", "B", "C"], [1, "X", True], [False, 12, 5.5]]

# a list of integers:
daily_step_count = [10343, 9385, 7029, 10931,5921]
print(daily_step_count[2])
#output would be 7029

daily_step_count[4] = 100
print(daily_step_count)
#output would be [10343, 9385, 7029, 10931, 100]

## LISTS - append()
#Appends the value 8694 to the end of the list.
daily_step_count.append(8694)
print(daily_step_count)
# outputs: [10343, 9385, 7029,10931, 5921, 100, 8694]

## LISTS - insert()
# Inserts the value 4473 before the current element 3
daily_step_count.insert(3, 4473)
# output: [10343, 9385, 7029, 4473, 10931, 5921, 100, 8694]

## LISTS - remove()
daily_step_count = [10343, 9385, 7029, 10931, 5921, 7029]

# Removes the firs occurence of 7029 from the list.
daily_step_count.remove(7029)
print(daily_step_count)
# output: [10343, 9385, 10931, 5921, 7029]

## LISTS - pop()
# Removes the last item from the list. 
#Captures it into the popped variable
popped = daily_step_count.pop()
print(daily_step_count)
# output: [10343, 9385, 10931, 5921]

print(popped)
# output: 7029

## LISTS - index()
daily_step_count = [10343, 9385,7029,10931,5921,5921]

#Sets index value to the index of the first 5921
index_value = daily_step_count
print(index_value)
# output: 4

#index_value = daily_step_count.index(9999)
# output: an exception occurs because the value 9999 does not rxist in the list

## List - count()
daily_step_count = [10343, 9385, 7029, 5921, 5921]

# Sets count to the number of occurences of 5921.
print(count)
# output: 2 

## List - sort()
daily_step_count = [10343, 9385, 7029,  10931, 5921]

# Sorts in ascending order. 
daily_step_count.sort()
print(daily_step_count)
# output: [5921, 7029, 9385, 10343, 10931]

# Sorts in decending order 
daily_step_count.sort(reverse = True)
print(daily_step_count)
# output [10931, 10343, 9385, 7029, 5921]

## List - reverse()
daily_step_count = [10343, 9385, 7029, 10931, 5921]

# Reverses the order of the items in the list 
daily_step_count.reverse()
print(daily_step_count)
# outputs: [5921, 10931, 7029, 9385, 10343]

red_river = ['R', 'R', 'C', ' ', 'P', 'o', 'l','y','t','e','c','h','n','i','c']

print(red_river[2: 12: 2]) # from 2 to 12, stepping by 2
# output: ['C', 'P', 'l', 't', 'c']

print(red_river[: 10: 1]) # from start (0) to 10, stepping by 1
# output: ['R', 'R', 'C', ' ', ' P', 'o', 'l', 'y', 't', 'e']

print(red_river[5: : 3]) # from 5 to end (14), stepping by 3
# output: ['o', 't', 'h', 'c']

print(red_river[::5]) # from start (0) to end (14), stepping by 3
# output:['R', 'o', 'c']

#RRC POLYTECHNIC
print(red_river[-1: -5: -1]) # from last (14) to 5tth last, stepping backwards by 1
# output: ['c','i','n','h']

## TUPLES
provinces_and_territories = ('BC', 'AB', 'MB', 'SK')
manitoba = provinces_and_territories[3]

print(manitoba)
# output MB

# The following line of code causes an exception: Tuple
# Elements cannot be modified
provinces_and_territories[3] = 'Manitoba'
tuple_without_parenthesis = 6 , 5, 3 
print(type(provinces_and_territories))
print(type(tuple_without_parenthesis))

single_tuple = ('one_item', )
another_singe = 77,

