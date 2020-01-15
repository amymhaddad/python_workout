# You are to write a function that takes a list of lists
# (just one element deep) and returns a flat, one-dimensional version of the list.


def flatten(mylist):
    return [number for numbers in mylist for number in numbers]


# print(flatten([[1,2], [3,4]]))    # [1,2,3,4]


print(sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], []))
