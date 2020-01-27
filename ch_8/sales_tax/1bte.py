# Problem 1
# Income tax in many countries is not a flat percentage, but rather the combination of different "brackets." So a country might not tax you on your first $1,000 of income, and then 10% on the next $10,000, and then 20% on the next $10,000, and then 50% on anything above that.
# Write a function that takes someone’s income and returns the amount of tax they will have to pay, totalling the percentages from various brackets.


tax_rates = {999: 0, 10000: 0.10, 20000: 0.20, 20001: 0.50}


def total_tax(income):

    income_reducer = income
    tax_amount = 0
    while income_reducer > 1000:

        tax_amount += tax_rates[income_reducer]
        income_reducer = income_reducer - 10000

    return int(tax_amount * income)


# Problem 2
# The dict.fromkeys method makes it easy to create a new dictionary. For example, dict.fromkeys('abc') will create the dict {'a':None, 'b':None, 'c':None}. You can also pass a value that will be assigned to each key, as in dict.fromkeys('abc', 5), resulting in the dict {'a':5, 'b':5, 'c':5}.
# Implement a function that does the same thing as dict.keys, but whose second argument is a function. The value associated with the key will be the result of invoking f(key).

numbers = [1, 2, 2, 3, 4]


def square_num(num):
    return num * 2


def create_dict():

    sq_num = {}
    for num in numbers:
        sq_num[num] = square_num(num)

    return sq_num
