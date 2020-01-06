import re

vowels = "aeiou"
with open("input_text.txt") as input, open(
    "output_vowels.txt", "w"
) as output_vowels, open("output_consonants.txt", "w") as output_consonant:
    each_line = input.readline()

    for letter in each_line.lower():
        validate_letter = re.sub(r"\W", "", letter)
        if validate_letter in vowels:
            output_vowels.write(validate_letter)
        else:
            output_consonant.write(validate_letter)
