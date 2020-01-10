# Write a program that asks the user to enter a simple math expression in prefix notation.
# Your program will parse the input and produce the appropriate output. It'll handle the six basic arithmetic operations in Python---addition, subtraction, multiplication, division (/), modulus (%), and exponentiation (**)
# The program will thus handle + 3 5 7 or / 100 5 5, and will apply the operator from left to right---giving the answers 15 and 4, respectively.

import operator, functools

user_input = "/ 100 5 5"

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "**": operator.pow,
}


def calculate(expression):
    operation, *args = user_input.split()
    numbers = [int(number) for number in args]

    return int(functools.reduce(operations[operation], numbers))


print(calculate(user_input))
