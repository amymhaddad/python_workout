# Create a dictionary -- using a dictionary comprehension -- whose keys are the (lowercase) letters of the English alphabet, and whose values are the numbers ranging from 1 to 26.

from string import ascii_lowercase as letters

gematria = {letter: digit for letter, digit in zip(letters, range(1, 27))}
print(gematria)
