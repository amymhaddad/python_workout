import os, re
from string import digits

# from pathlib import Path

# def longest_word():
#     files_longest_words = {}
#     totals = {}

#     all_books = list(Path('./books').iterdir())
#     for book in all_books:
#         for i, lines in enumerate (open(book)):
#             validated_lines = re.sub(r'\W+', " ", lines)
#             if validated_lines.startswith(("http", "\n", digits)):
#                 continue

#             else:
#                 try:
#                     for word in validated_lines.split():
#                         totals[word] = len(word)

#                 except KeyError:
#                     continue

#         max_length = max([value for value in totals.values()])
#         for word, length in totals.items():
#             if length == max_length:
#                 files_longest_words[book] = max_length
#         totals = {}
#     return files_longest_words

# print(longest_word())

import os

dirname = input("Enter a directory name: ")

# fucntion summary:
# iterate over every line of a file, and then over every word in the line. If we find a word that’s longer than the current longest_word, then we replace the old word with the new one.


def find_longest_word(filename):
    longest_word = ""
    # cycle through each line of file
    for one_line in open(filename):
        # cycle through each line and grab each word
        for one_word in one_line.split():
            # see if the length of each word is GREATER than the currently empty string
            if len(one_word) > len(longest_word):
                # IF the word is greater, than replace the longest_word with one_word
                longest_word = one_word
    return longest_word


total = {
    filename: find_longest_word(os.path.join(dirname, filename))
    for filename in os.listdir(dirname)
    if os.path.isfile(os.path.join(dirname, filename))
}


print(total)


# #This is a dictionary comp.
# #Create a dictionary based on iterating over a source. The source, in our case, will be a list of filenames
# #Use comprehensions when you need to transform a collection of inputs into a collection of outputs
# #Think of os.path.join as a filename-specific version of str.join
# print({filename : find_longest_word(os.path.join(dirname, filename))

#        #The code below is just to iterate theorugh the list of file grab a valid file
#         #iterate over all files in dir
#        for filename in os.listdir(dirname)
#        #test to see if the filename IS a FILE
#        #os.path.isfile() --> Returns True if path is an existing regular file.  Do this bc ONLY want FILES
#        if os.path.isfile(os.path.join(dirname, filename))   })

# #{filename, which is hte name I passed in: functionthat finds the longest word(joins dir name and filenema -->./books/pride.txt)}

# #dict comp workflow:
# #1. Iterate over the list of files in the directory; put the filename in the vairable "filename"
# #for filename in os.listdir(dirname)  --> {filename: }

# #2. For each file, run find_longest_word() function and pass in filename as the arg.
# #The return value is a string -- the longest string in teh file

# #3. Each filename and the longest-word combination becomes a k, v pair
