# Exercise 1:
# Given a string containing several (space-separated) words,
# create a dict in which the keys are the words, and the values are the number of vowels in each word.
# If the string is 'this is an easy test', then the resulting dict would be {'this':1, 'is':1, 'an':1, 'easy':2, 'test':1}.

from collections import Counter


string = "this is an easy test"
vowels = "aeiou"

dict = {}
counter = 0
for word in string.split(" "):
    for letter in word:
        if letter in vowels:
            counter += 1

    dict[word] = counter
    counter = 0

# print(dict)

# My attempt at trying to use Counter to count the number of vowels being used in each word
# Currently, I get a count of each letter in each word, when all I need is the count of the vowels for each word:
# {'this': Counter({'t': 1, 'h': 1, 'i': 1, 's': 1}), 'is': Counter({'i': 1, 's': 1}), 'an': Counter({'a': 1, 'n': 1}), 'easy': Counter({'e': 1, 'a': 1, 's': 1, 'y': 1}), 'test': Counter({'t': 2, 'e': 1, 's': 1})}
def most_vowels(words):
    repeats = {word: Counter(word) for word in words.split(" ")}
    return repeats


# print(most_vowels(string))


# Exercise 2:
# Create a dictionary whose keys are filenames and whose values are the lengths of the files. The input can be a list of files from os.listdir or glob.glob

import sys, os

files = os.listdir("/Users/amyhaddad/python/python_workout/ch_4/flip_dict")

file_length = {file: len(file) for file in files}


# Exercise 3:
# Find a configuration file in which the lines look like "name=value".
# Use a dict comprehension to read from the file, turning each line into a key-value pair.
# (If you wish, you can do this for Unix’s /etc/passwd file, creating a dict from the usernames (index 0) and user ID number (index 2) on each line containing a user record.


def read_config_file(file):
    with open(file) as f_object:
        return f_object.readlines()


def create_name_value_dictionary(rows):
    name_values = {}
    unique_row = [row.split("=") for row in rows]
    return {item[0]: item[-1] for item in unique_row}


print(create_name_value_dictionary(read_config_file("config_file.txt")))
