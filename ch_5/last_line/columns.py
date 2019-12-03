# Create a text file (using an editor, not necessarily Python) containing two tab-separated columns, with each column containing a number.
# Then read through the file you have created with Python.
# For each line, multiply each number by the second, and then sum the results.
# Ignore any line that doesn’t contain two numeric columns.


import csv


def create_number_list():
    """Put each row from a CSV files in its own list"""

    row_numbers = []
    with open("numbers.txt", newline="") as csvfile:
        linereader = csv.reader(csvfile, delimiter=" ")
        for row in linereader:
            row_total = []
            for item in row:
                if item.isdigit():
                    row_total.append(int(item.strip(" ")))
            row_numbers.append(row_total)
    return row_numbers


def calculate_rows():
    """Multiply the numbers in the columns and add them together"""
    total = []

    row_numbers = create_number_list()

    for number in row_numbers:
        if number:
            for num in number:
                multi_ints = number[0] * number[1]
            total.append(multi_ints)
    return sum(total)


print(calculate_rows())
