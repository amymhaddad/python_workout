# Iterate over the lines of a text file. 
# Find all of the words (i.e., non-whitespace surrounded by whitespace) that contain only integers, and sum them.

import re


numbers = []
for lines in open('text_file.txt'):
    for word in lines.split(" "):
        
        validate_word = re.sub(r'\D{1,}', '', word)

        if validate_word.isdigit():
            numbers.append(int(validate_word))
print(sum(numbers))