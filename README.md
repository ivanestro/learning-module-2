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
#output: Hello World!
- Printing multiple values:
print("I am", 25, "years old.")
#output: I am 12 years old.
- Multiple values separated by commas:
print("apples", "oranges", "bananas", sep = ",")
#output: apples, oranges, bananas

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
Type conversios are temporary unless used in conjuction with an assignment operator.

## Constants 

- In python, as opposed to most other program language, there is no built in concept of a "constant"
- A constant typically defined as a variable whose value remains the same throughout the program and should not be modifed. 
Most other programming langauge will enforce this and ensure constands are not modified.
- In Python, we can instead denote values that should constant by using an uppercase name for the variable and not modifying its value once it has been set. 
[EOF]
