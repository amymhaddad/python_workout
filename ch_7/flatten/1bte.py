# You are to write a function that takes a list of lists (just one element deep) and returns a flat, one-dimensional version of the list.
# The output only contains odd integers.
# Inputs that are neither odd nor integers should be excluded. Inputs containing strings that could be converted to integers should be converted; other strings should be excluded.

x = [[1, 2, 3], [9, 7, 9], ["3", "5", "cat"]]

# Option 1
def flatten_odd(number_lists):
    return [
        int(number)
        for numbers in number_lists
        for number in numbers
        if isinstance(number, int) or number.isdigit()
    ]


# Option 2
odds = [int(num) for num in sum(x, []) if isinstance(num, int) or num.isdigit()]
