# Problem 1:
# You have a range of integers, from 0-15. You would like to print those numbers on the screen, with commas between them.
# num_list = [num for num in range(0, 15)]
# string_of_nums = ", ".join([str(num) for num in num_list])


# Problem 2:
# take a list of integers and turn them into strings. However, you’ll only want to produce strings for integers between 0 and 10.

# num_list = range(15)
# first_ten = ", ".join([str(num) for num in num_list if num <= 10])

# print(first_ten)


# Problem 3:
# Given a list of strings containing hexadecimal numbers, sum the numbers together.

# hex_strings = ['0x1', '0x2', '0x3']

# sum_nums = sum([int(num, 0) for num in hex_strings])


# Problem 3:
# Use a list comprehension to reverse the word order of lines in a text file.

# Option 1:
lines = [line.strip().split(" ") for line in open("letters.txt").readlines()]

reversed_list = [line[::-1] for line in lines]

# Option 2
total = [
    rev for line in open("letters.txt").readlines() for rev in line.strip().split(" ")
][::-1]


print(total)
