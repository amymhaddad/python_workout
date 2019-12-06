# Exercise 1
# Write a function that takes a float and two integers (before and after).
# The function should return a float consisting of before digits before the decimal point and after digits after.
# Thus if we call the function with 1234.5678, 2 and 3, the return value should be 34.567.


def reduce_floats(float, before, after):
    float = str(float)
    decimal_point = float.find(".")

    first_half = float[:decimal_point]
    second_half = float[decimal_point + 1 :]

    return f"{first_half[-before:]}.{second_half[:after]}"


# Exercise 2
# Write a function that takes two strings from the user,
# turns them into Decimal instances, and then prints the floating-point answer.
# In other words, make it possible for the user to enter 0.1 and 0.2, and for us to get 0.3 back.

from decimal import Decimal


def add_floats(str1, str2):
    return Decimal(str1) + Decimal(str2)


print(add_floats("0.1", "0.2"))
