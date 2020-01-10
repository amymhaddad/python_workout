import operator

user_input = input("Enter a math calculation in prefix notation: ")

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "**": operator.pow,
}


operator, num1, num2 = user_input.split()
print(operations[operator](int(num1), int(num2)))
