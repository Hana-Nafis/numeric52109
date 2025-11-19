###
## simple_package - Module operations.py
## Basic online calculator
###

## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface function
##    that will prompt the user for input and
##    call the appropriate function based on the
##    user's input. The interface function should
##    continue to prompt the user for input until
##    the user enters'exit'. 
##
## 2) The interface function should also handle
##    any exceptions that might be thrown by the
##    basic operations functions. If an exception 
##    is thrown,the interface function should print 
##    an error message and continue to prompt the 
##    user for input.
##
## 3) Add other "operations" to the calculator, that
##    involve complicated operations (e.g., 
##    trigonometric functions, logarithms, etc.).
##

"""
operations.py
---------------
Module containing basic and advanced mathematical operations for the simple_package calculator. 
Includes addition, subtraction, multiplication, division, percentage, powers, exponentials, trigonometric functions, and logarithms.
Also provides a user-facing calculator interface that allows interactive operation input until the user exits.
"""


import math

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def percent(a, b):
    """Calculate what percent a is of b."""
    if b == 0:
        raise ZeroDivisionError("Cannot calculate percentage with denominator zero.")
    return (a / b) * 100

def power(a, b):
    """Raise a to the power of b."""
    return a ** b

def exponential(a):
    """Calculate the exponential of a number."""
    return math.exp(a)

def sine(a):
    """Calculate the sine of a number."""
    return math.sin(a)

def cosine(a):
    """Calculate the cosine of a number."""
    return math.cos(a)

def tangent(a):
    """Calculate the tangent of a number."""
    return math.tan(a)

def logarithm(a, base=math.e):
    """Calculate the logarithm of a number with a given base."""
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log(a, base)

def calculator_interface():
    """Interface function for the calculator."""
    help_text = """
Welcome to the simple calculator!

Available operations:
  add a b         → addition
  subtract a b    → subtraction
  multiply a b    → multiplication
  divide a b      → division
  percent a b     → a is what % of b
  power a b       → a^b
  exponential a   → e^a
  sine a          → sin(a)
  cosine a        → cos(a)
  tangent a       → tan(a)
  logarithm a b   → log base b (default = e)

Type 'help' to see this list again.
Type 'exit' to quit.
"""
    print(help_text)
    
    while True:
        user_input = input("Enter operation and numbers (e.g., 'add 2 3'): ")
        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        if user_input.lower() == 'help':
            print(help_text)
            continue
        
        try:
            parts = user_input.split()
            operation = parts[0]
            numbers = list(map(float, parts[1:]))

            if len(numbers) < 1:
                print("Not enough numbers provided.")
                continue
            if operation in ["add","subtract","multiply","divide","percent","power"] and len(numbers) != 2:
                print("This operation requires TWO numbers.")
                continue



            if operation == 'add':
                result = add(numbers[0], numbers[1])
            elif operation == 'subtract':
                result = subtract(numbers[0], numbers[1])
            elif operation == 'multiply':
                result = multiply(numbers[0], numbers[1])
            elif operation == 'divide':
                result = divide(numbers[0], numbers[1])
            elif operation == 'percent':
                result = percent(numbers[0], numbers[1])
            elif operation == 'power':
                result = power(numbers[0], numbers[1])
            elif operation == 'exponential':
                result = exponential(numbers[0])
            elif operation == 'sine':
                result = sine(numbers[0])
            elif operation == 'cosine':
                result = cosine(numbers[0])
            elif operation == 'tangent':
                result = tangent(numbers[0])
            elif operation == 'logarithm':
                if len(numbers) == 2:
                    result = logarithm(numbers[0], numbers[1])
                else:
                    result = logarithm(numbers[0])
            else:
                print("Unknown operation. Please try again.")
                continue

            print(f"The result is: {result}")

        except Exception as e:
            print(f"Error: {e}. Please try again.")