"""Find the word with the greatest number of repeated vowels."""

from collections import Counter

words = ["ttttttttttest", "program", "iiiiis"]
vowels = "aeiou"


# Option 1
repeated_vowels = {
    word: max(Counter(word).items(), key=lambda pair: pair[1]) for word in words
}
print(max(repeated_vowels, key=lambda w: repeated_vowels[w][0] in vowels))


# Option 2
def most_repeating_letter_count(word):
    for letter in word:
        return Counter(word).most_common()


def most_vowels(words):
    repeats = {word: most_repeating_letter_count(word) for word in words}
    return max(repeats, key=lambda x: x[0] in vowels)


print(most_vowels(words))
