numbers = [10, 20, 30, 40, 50, 60]

# Write a function that takes a list or tuple of numbers.
# Return a two-element list, containing (respectively) the sum of the even-indexed numbers
# and the sum of the odd-indexed numbers. So calling the function as even_odd_sums([10, 20, 30, 40, 50, 60]), you’ll get back [90, 120].


def sum_even_indexed_numbers(numbers):
    even_index = []
    odd_index = []
    for i, number in enumerate(numbers):
        if (i == 0) or (i % 2 == 0):
            even_index.append(number)
        else:
            odd_index.append(number)

    return [sum(even_index), sum(odd_index)]


print(sum_even_indexed_numbers(numbers))


# Write a function that takes a list or tuple of numbers.
# Return the result of alternately adding and subtracting numbers from each other.
# So calling the function as plus_minus([10, 20, 30, 40, 50, 60]), you’ll get back the result of 10+20-30+40-50+60, or 50.


def plus_minus(numbers):

    update_number = 0

    for i, num in enumerate(numbers):

        if (i == 0) or (i % 2 != 0):
            update_number += num
        else:
            update_number = update_number - num
    return update_number


print(plus_minus(numbers))


# Write a function that emulates the builtin zip function, taking any number of iterables and returning a list of tuples.
# Each tuple will contain one element from each of the iterables passed to the function.
# Thus, if I call myzip([10, 20,30], 'abc'), the result will be [(10, 'a'), (20, 'b'), (30, 'c')]. You can return a list (not an iterator),
# and can assume that all of the iterables are of the same length.

one = [10, 20, 30]
two = "abc"


def myzip(iter1, iter2):
    return list(zip(iter1, iter2))


print(myzip(one, two))
