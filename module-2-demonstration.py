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

## SLICING
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
tuple_without_parenthesis = 6, 5, 3
print(type(provinces_and_territories))  # <class 'tuple'>
print(type(tuple_without_parenthesis))  # <class 'tuple'>

single_tuple = ('one_item', )
another_single = 77,

provinces_and_territories = ('BC', 'AB', 'MB', 'SK')
manitoba = provinces_and_territories[3]

print(manitoba)  # output: MB

#The following line of code causes an exception:Tuple
# elements cannot be modified
provinces_and_territories[3] = "Manitoba"

# use assignment to modify tuple:
provinces_and_territories = ('BC', 'AB', 'MB', 'SK')

random_tuple = (1, 66, 3, 7, 42, 78, 12, 55)

## TUPLES - LENGTH()
length = len(random_tuple)
print(length) # output: 8

## TUPLES - MAX()
max = max(random_tuple)
print(max)  # output: 78

## TUPLES- MIN()
min = min(random_tuple)
print(min) # output: 1

## TUPLES SUM()
sum = sum(random_tuple)
print(sum)  # output: 264

## TUPLES - SORTED()
sorted_tuple = sorted(random_tuple)
print(sorted_tuple)  # output: [1, 3, 7, 12, 42, 55, 66, 78]
# output: [1, 3, 7, 12, 42, 55, 66, 78]

## TUPLES - TUPLE()
name = "Ivan"
tuple_name = tuple(name)
print(tuple_name)
# output: ('I', 'v', 'a', 'n')

list_of_numbers = [1,2,3]
tuple_of_numbers = tuple(list_of_numbers)
print(tuple_of_numbers) 
# output: (1, 2, 3)

## DICTIONARIES
# Examples of Dictionaries in action:
fruit_inventory = {'apples': 23, 'oranges': 10, 'bananas': 59}

value = fruit_inventory['oranges']
print(value) # output: 10

fruit_inventory['oranges'] = 25
print(fruit_inventory['oranges']) # output: 25

fruit_inventory['plums'] = 100 # adding a new key-value pair


print(fruit_inventory)
# output: {'apples': 23, 'oranges': 25, 'bananas': 59}

## DICTIONARIES - KEYS()
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
car["color"] = "white"

print(x)
# output: dict_keys(['brand', 'model', 'year', 'color'])

## DICTIONARIES - VALUES()

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
car["year"] = 2018
print(x)
# output: dict_values(['Ford', 'Mustang', 2018])

## DICTIONARIES - ITEMS()
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items() 
car["year"] = 2018
print(x)
# output: dict_items([('brand', 'Ford'),('model', 'Mustang'), ('year', 2018)])

## DICTIONARIES - GET()
print(fruit_inventory.get('apples'))  # output: 23

print(fruit_inventory.get('pears', 'Fruit is not in dictionary')) # output: Fruit is not in dictionary

print(fruit_inventory.get('pears'))
# output: None (no default value provided)

## DICTIONARIES - POP()
fruit_inventory.pop('oranges')
print(fruit_inventory)
# output: {'apples': 23, 'bananas': 59}

## DICTIONARIES - CLEAR()
fruit_inventory.clear() 
print(fruit_inventory)
# output: {}

## SETS 
primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}
fives = set()

## SETS - ADD() 
primes.add(29)
fives.add(5)

print(primes)  # output: {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
print(fives)  # output: {5}

## SETS - REMOVE()
primes.remove(3)
print(primes) # output: {2, 5, 7, 11, 13, 17, 19, 23, 29}

primes.remove(22) # This will raise a KeyError since 22 is not in the set

## SETS - DISCARD()
primes.discard(2)
print(primes)  # output: {5, 7, 11, 13, 17, 19, 23, 29}

primes.discard(22) # No exception occurs

## SETS - UNION()
union = primes.union(fives)
print(union)  # output: {2, 5, 7, 11, 13, 17, 19, 23, 29}

## SETS - DIFFERENCE()
difference = primes.difference(fives)
print(difference) # output: {2, 7, 11, 13, 17, 19, 23, 29}

difference = fives.difference(primes)
print(difference) 
# output: {35, 10, 15, 20 ,25 ,30}

## SETS - INTERSECTION()
intersection = primes.intersection(fives)
print(intersection) # output: {5}