# Ex 2:
# Ask the user to enter integers, separated by spaces.
# From this input, create a dictionary whose keys are the factors for each number,
#  and the values are lists containing those of the users' integers that are multiples of those factors.


def get_factors(string):
    factors_multiples = {}
    factors = ()

    user_numbers = [int(number) for number in string.split(",")]

    for i, numbers in enumerate(user_numbers):
        for number in range(1, numbers + 1):
            if number * numbers == user_numbers[i]:
                factors += (number, numbers)
                factors_multiples[factors] = []

        factors = ()
    return factors_multiples


def get_multiples(factors_multiples, string):

    index = 0
    for factors, multiples in factors_multiples.items():
        for factor in factors:
            multiple = factor * index
            if str(multiple) in string:
                multiples.append(multiple)
                index = 0
            else:
                index += 1
        index = 0
    return factors_multiples
