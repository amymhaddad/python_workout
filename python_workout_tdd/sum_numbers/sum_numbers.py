# EXERCISE 1
# The challenge here is to write a mysum function that takes a variable number of arguments as a list. If a second argument is provided, this is the starting point for the summing of the numbers.
# So sum([1,2,3], 4) returns 10, because 1+2+3 is 6, and would be added to the starting value of 4.
# If a second argument is not provided, then it should default to 0. You should not use the built-in sum function to accomplish this


def mysum(number_list, start_value=0):
    total = 0

    for number in number_list:
        total += number
    return total + start_value


# EXERCISE 2
# Write a function that takes a list of numbers.
# It should return the average (i.e., arithmetic mean) of those numbers.


def list_average(number_list):

    total = 0
    for number in number_list:
        total += number
    return total // len(number_list)


# EXERCISE 3 -- option 1
# Write a function that takes a list of words (strings).
# It should return a tuple containing three integers,
# representing the length of the shortest word, the length of the longest word, and the average word length.


def word_length(word_list):

    word_results = (
        len(min(word_list, key=lambda x: len(x))),
        len(max(word_list, key=lambda x: len(x))),
    )

    word_lengths = 0

    for word in word_list:
        word_lengths += len(word)
    word_results += (word_lengths // len(word_list),)
    return word_results


# EXERCISE 3 -- option 2


def word_length(word_list):

    lengths = [len(word) for word in word_list]
    return (min(lengths), max(lengths), sum(lengths) // len(word_list))


# EXERCISE 4
# Write a function that takes a list of Python objects.
# Sum the objects that either are integers or can be turned into integers, ignoring the others


def sum_ints(object_list):

    total = 0
    for item in object_list:
        if isinstance(item, int):
            total += item
        elif item.isdigit():
            total += int(item)
    return total
