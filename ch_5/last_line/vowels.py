# Read through a text file, line by line. Use a dict to keep track of how many times each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation.

vowel_counter = {}
vowels = "aeiou"

with open("text_file.txt") as f_object:
    for letter in f_object.readline().lower():
        if letter in vowels:
            vowel_counter[letter] = vowel_counter.get(letter, 0) + 1

for vowel, count in vowel_counter.items():
    print(vowel, count)
