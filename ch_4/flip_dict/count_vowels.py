#Exercise 1:
# Given a string containing several (space-separated) words, 
# create a dict in which the keys are the words, and the values are the number of vowels in each word. 
# If the string is 'this is an easy test', then the resulting dict would be {'this':1, 'is':1, 'an':1, 'easy':2, 'test':1}.

string = "this is an easy test"
vowels = "aeiou"

dict = {}
counter = 0
for word in string.split(" "):
    for letter in word:
        if letter in vowels:
            counter+= 1

    dict[word] = counter
    counter = 0

# print(dict)


#Exercise 2:
# Create a dictionary whose keys are filenames and whose values are the lengths of the files. The input can be a list of files from os.listdir or glob.glob

import sys, os

files = os.listdir('/Users/amyhaddad/python/python_workout/ch_4/flip_dict')

file_length = { file: len(file) for file in files}


#Exercise 3:
# Find a configuration file in which the lines look like "name=value". 
# Use a dict comprehension to read from the file, turning each line into a key-value pair. 
# (If you wish, you can do this for Unix’s /etc/passwd file, creating a dict from the usernames (index 0) and user ID number (index 2) on each line containing a user record.

name_values = {}
with open ('config_file.txt') as f_object:
    row = f_object.readlines()
    for items in row:
        for item in items.split(":"):
        #    print([item][1])
            # name_values[item][0] = name_values[item][1]

# print(name_values)

# ('_reportmemoryexception:*:269:269:ReportMemoryException:/var/db/reportmemoryexception:/usr/bin/false\n', '')
