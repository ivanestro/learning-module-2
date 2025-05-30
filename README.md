### Learning Module 2

## Description

Introduction to Python: Documentation, Variables, Printing

## Author

Ivan Estropigan

## What is Software Development?

- Computer Programming
- Designing, writing, testing and maintaining computer software.
- Using programming languages to create instructions that computer can understand and execute.
Humans go bla-bla-bla, computers go beep-boop
- These instructions can range from simple calculations to complex algorithms that control how computer interacts with its hardware and other software.

## What is Python?

- Python is high level interpreted programming language.
Focuses on simplicity, readability and ease of use.
- It is a dynamically-typed language, meaning that variables do not need to be declared with a specific data type before they are used.
You don't need to specify that "age" will be a number before setting it to be a number.
- Python has a large standard library of pre-written code, which provides a wide range of functions and tools that can be used to accomplish a variety of tasks.
- It is widely used in web development scientific computing, data analysis, artificial intelligence, machine learning and many other areas.
See the notes for more info on 'Interpreted', 'open-source', 'syntax', and 'dynamically-typed'.

## What is Syntax?

- Syntax refers to the set of rules that define how programming language should be structured and written in order for the computer to understand and execute it correctly.
Similar to how human languages are structured so that people understand each other.
- These rules govern how keyboards, operators, functions and other elements of the language can be combined to create valid program statements.
Like nouns, verbs, adjectives etc
- A violation of these rules result in a syntax error. Syntax Errors are one type of error that can occur in software development.
Like French, computers can't deal with imperfect speech.

## What are standards?

- Software development standards (aka: coding standards or coding conventions) are a set of best practices that are used to ensure consistent and readable code across a development team or organization.
- Many software development standard are language-specific. That is standards for one language will differ from other languages. While other standards transcend languages.
Think of the standard form of english poems vs japanese haikus.
- Software development standards cover wide range of topics, including naming conventions, code formatting, documentations, commenting and error handling.
- These standards ensure that code is easy to understand, maintain, and produces efficient results. Standards support software maintenance.
- Python Enhancement Proposals 8 (PEP *)
- Covers such as:
Code layout
String Quotes
Whitespace in Expressions and Statements
Comments
Naming Conventions

## Documentation

- Documentation in Python refers to the written information, guides, and examples that explain how to use particular module, function or program.
- DOCstring (""" """) are inline documentation that describes the purpose and usage of a Python function or class.
They are typically enclosed in triple quotes and placed at the beginning of the function or class.
In Software Development Fundamentals, a docstring similar to the one shown in the previous slide will be included at the top of every file created.
As the course progresses, additional docstring will be created to document functions, classes and methods.

## Documentation vs Commenting

- Documentation in Python refers to the written information, guides, and examples that explain how to use a particular module, function or program
Standard is to put them at the start of the module, function, or program that is documented.
- Comments are similar but are found mixed with the code to explain it to the reader.
- Documentation is like the text on the back of a book or movie case, comments are like the commentary of footnotes inside.
    #This is a single line comment.
    """
    This is a multi-line comment.
    It can span multiple lines.
    """

## Functions

- Functions will have an entire module dedicated to them.
Here's a teaser for now example - Hello World.
- Functions are pieces of code that are written so that they can be invoked as a single line.
Who here knows how to tie their shoes?
- Function in Python are named using lowercase letters
If the function contains more than one word in the name, the lowercase words will be separated by underscores.
- Functions may receive one or more arguments, which are input values that are passed to the function.
These Parameters are defined within parentheses following the function name.
Since Python is a dynamically typed language, the datatype of the argument is not enforced, but passing data of the of the wrong typed could lead to unexpected results.
- Functions are pieces of code that are written so that they can be invoked as a single line
Who here knows how to tie their shoes?
- Functions in Python are named using lowercase letters
If the function contains more than one word in the name, the lowercase words will be separated by underscores.
- Functions may receive one or more argument, which are input values that are passed to the function.
These parameters are defined within the parentheses following the function name.
Python is dynamically typed, the datatype is not enforced, but passed data of the wrong type could lead to unexpected results.
- The return value is the output value that is returned by the function when it completes its task.
Some functions do not return a value and simply perform actions, while others return one or more values.

## Print Function

- Most common function you'll use outputs text to the console
print(*objects, sep = ' ', end = '\n', file= sys.stdout, flush = false)
- Objects: You can pass one or more objects to the function to be printed, separated by commas. The objects can be of any data type.
- Sep: The separator used to separate the objects in the output. By default, iti s a space ('')
- End: The string appended at the end of the output. By default, it is a newline character ("\n"), so each print() call will output on a new line.
- File: The file object where output is sent. By default, it is set to sys.stdout, the console. The output can be redirected to a file by specifying a file object (More on File Output in a later module).
- Flush: A boolean flag that specifies wether to flush the output buffer after printing. By default, it is set to False, so the output buffer is not immediately flushed.
- Printing a single value:
print("Hello World!")
- #output: Hello World!
- Printing multiple values:
print("I am", 25, "years old.")
- #output: I am 12 years old.
- Multiple values separated by commas:
print("apples", "oranges", "bananas", sep = ",")
- #output: apples, oranges, bananas

## Print with F-Strings

- An f-string, or formatted string, allows us to create dynamic strings easily by embedding expressions in them
<br Not limited to printing, but used in many cases. />
"""

"""

## Variables

- A variable is named reference to a value or an object.
- Variables are used to store data in computer memory so that it can be referenced and used later in a program.
Aka: a container of data with a label on it

- A dynamically-typed language (like Python) determines the data type of a variable at runtime based on the value it is assigned.

## Simple Data Types

- Numeric data types are used to represent numbers. In python, there are three data types:
- int(integer): whole numbers, no decimal points
- float(floating-point number): decimal points and can use exponents, think scientific notation.
- complex(complex number): not used in this course.
- text: data types are used to represent strings of characters.
- boolean: in python the bool (Boolean) data types are used to represent truth values True or False.

## Type Conversions

- Type conversion (also known as type casting or data type conversion) refers to the process of converting a value from one data type to another.
This is often necessary when the type of data being used is not compatible with the operation or function being performed on it.
For example, if you have a string containing a number, you may need to convert it ot an integer or a float to perform mathematical operations on it.
- Type conversion can be implicit or explicit.
Implicit type conversion, also known as type coercion, occurs when the programming language automatically converts one data type to another without the need for explicit instructions from the programmer.
Type conversion are temporary unless used in conjunction with an assignment operator.

## Constants

- In python, as opposed to most other program language, there is no built in concept of a "constant"
- A constant typically defined as a variable whose value remains the same throughout the program and should not be modified.
Most other programming language will enforce this and ensure constants are not modified.
- In Python, we can instead denote values that should constant by using an uppercase name for the variable and not modifying its value once it has been set.

## Standard Operators

- Here are some of the common operators in Python:
- "=" Assignment to set the value of a variable
- "+" Addition to sum two numbers, also used with text Strings for concatenation (combining text together)
- "-" Subtraction to get the difference of two numbers
- "*" Multiplication to get the product of two numbers
- "/" Division to get the quotient of two numbers, with decimal
- "//" Floor division to get the quotient of two numbers, with no decimal (aka: integer division)
- "%" Modulus to get the remainder of the division of two numbers
- "**" Exponentiation to get the results of the first number to the power of the second.

- "/" result = 42/ 4 result = 10.5
- "//" Floor Division result = 42 // 4 result = 10
- "%" Modulus to get the remainder of the division of two numbers result = 100 % 55 result = 45
- "**" Exponentiation to get the result of the first number to the power of the second result 2** 4 result = 16
- "+=" Combines addition and assignment into a single operator age += 1 same as : age = age + 1
- "-=" Combines subtraction and assignment into a single operator. count -= 1 same as: count = count - 1
- "*=" Combines multiplication and assignment into a single operator factor* = 10 same as: factor = factor * 10
- "/=" Combines division and assignment into a single operator half /= 2 same as: half = half / 2
- "//=" Combines floor division and assignment into a single operator third // = 3 same as third = third // 3
- "%=" Combines modulus and assignment into a single operator remainder %= 2 same as: remainder = remainder % 2
- "**" Combines exponentiation and assignment into a single operator power** = 3 same as: power = power = ** 3

## Order of Operations

- The order of operation rules in Python dictate the order in which the arithmetic operations are evaluated.
- These rules are similar to the rules of arithmetic you are familiar with (BEDMAS)
- Parentheses: expressions within parentheses are evaluated first
- Exponentiation: expressions with Exponentiation are evaluated second
- Division, Multiplication and Modulus: these operations are evaluated third if there are multiple items of this category, they are executed from left to right
- Addition and Subtraction: these operations are evaluated last if there are multiple items of this category, they are executed from left to right.
- result = ((10 + 5) * 2) / 3 result = 10.0
- versus: result = 10 + 5 * 2 / 3 result = 13.3^
- Assignment to variables is the final step

## Python Collection Types

- A collection is an object that contains multiple elements or items of data
Think a box of eggs or a car parking lot
- There are four main types of built-in collections in Python:
- Lists: A list is an order (But not necessarily sorted) collection of elements, and it is mutable (can be modified.)
- Tuples: a tuple is an ordered collection of elements, similar to a list, but it is immutable (cannot be modified.)
- Dictionaries: A dictionary is an unordered collection of key-value paris, and it is mutable.
- Sets: A set is an unordered collection of unique elements and it is mutable.

## Lists

- A list is a built in data structure used to store a collection of items, which can be of different data types.
- Lists are defined by enclosing a comma-separated sequence of values in square brackets.

## Lists - append()

- As the name implies, append() adds to the end of a list
- Note that this is a method that belongs to the list class and therefore uses dot notation (in contrast to functions like print, type and abs)

## Lists - insert()

- As the name implies, insert() adds to a given location in a list
- Note that this is a method that belongs to the list class and therefore uses dot notation (In contrast to functions like print, type and abs)

## Lists - remove()

- As the name implies, remove() deletes a specific items from a list
- Note that this is a method that belongs to the list class and therefore uses dot notation (in contrast to functions like print, type, and abs)

## Lists - pop()

- Like removing a bottle cap or lid, pop() removes (and returns) the last item from the list
- Note that this is a method that belongs to the list class and therefore uses dot notation (in contrast to functions like print, type, and abs)

## Lists - index()

- Like the index at the end of a book, index() tells us the location of an item in the list
- Note that this is a method that belongs to the list class and therefore uses dot notation (in contrast to functions like print, type and abs)

## List - count()

- Like a muppet, count() tells us how many items of a certain value there are in the list
- Note that this is a method that belongs to the list class and therefore uses dot notation (in contrast to functions like print, type and abs)

## List - sort()

- Like organizing a set of playing cards, sort() puts the items in the list in a specific order
- Note that this is a method that belongs to the list class and therefore uses dot notation (in contrast to functions like print, type and abs)

## List - reverse()

- Flip everything around, reverse() puts the items in the list in the opposite order
- Note that this is a method that belongs to the list class and therefore uses dot notation (in contrast to functions like print. type and abs)

## Slicing

- Slicing is a way to extract a subset of elements from a sequence object (such as a string, list, or tuple) by specifying a range of indices.
- start is the index of the first element to be included in the slice (inclusive). If the start value is excluded the beginning of the list (position 0) is assumed.
- stop is the index of the last element to be included in the slice (exclusive). If the stop value is excluded the end of the list is assumed
- step is the stride or interval between elements in the slice. If the step value is excluded, the default step value is 1.
-Negative values can also be used when slicing. The value of -1 is equivalent to the last item in the list, -2 is the second lsat item and so on.
- Slicing is a way to extract a subset of elements from a sequence object (such as a string list, or tuple) by specifying a range of indices.

## Tuples

- A tuple is an ordered, immutable sequence of elements.
- Tuples are similar to lists, but once a tuple is created, its contents cannot be changed.
- This means that you an use a tuple to store a collection of values that should not be modified during the lifetime of a program.
- When defining a tuple, its elements are enclosed in parentheses are separated by commas.
- If a tuple contains only a single element, that element must be followed by a comma.
- While tuples cannot be changed once created, new tuples can be created or an existing tuple can have its values re-assigned using the assignment operator.
- When defining a tuple, its element are enclosed in optional parentheses and separated by commas.
- If a tuple contains only a single element, that element must be followed by a comma.
- Tuples are similar to lists, but once a tuple is created its contents cannot be changed.
- While tuples cannot be changed once created, new tuples can be created or an existing tuple can have its value re-assigned using the assignment operator. Effectively completely replacing the tuple.
[EOF]
