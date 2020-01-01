# Write a dictionary to a CSV file. Each line in the CSV file should be: (1) the key, which we’ll assume to be a string, (2) the value, (3) the type of the value (e.g., str or int).

import csv

letters_and_numbers = {"a": 1, "b": "second", "c": 3}


with open("dict_csv.csv", "w", newline="") as csvfile:
    fieldnames = ["key", "type-of-value"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter="\t")

    writer.writeheader()
    for key, value in letters_and_numbers.items():
        writer.writerow({fieldnames[0]: key, fieldnames[1]: type(value)})
