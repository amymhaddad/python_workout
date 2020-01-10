# Write a function, apply_to_each, which takes two arguments:
# A function that takes a single argument, and an iterable.
# Return a list whose values are the result of applying the function to each element in the iterable.

# def sum_nums(seq):


def double(num):
    return num * 2


def apply_to_each(action, sequence):

    return [action(item) for item in sequence]


print(apply_to_each(double, [1, 2, 3]))
