def factorial(*args):

    total = 1
    for number in args:
        total *= number
    return total


print(factorial(1, 2, 3, 4))
