# Show the lines of a text file that contain at least one vowel and contain more than 20 characters.

import re

filter_lines = [
    line
    for line in open('text_file.txt').readlines()
    if re.findall(r"['aeiou]+", line) and len(line) > 20
]
