
from collections import Counter

words = ['thiiiiis', 'issssssss', 'a', 'ttttttttttest', 'program']
vowels = "aeiou"


def repeated_vowels(words):
    return { word: max(Counter(word).items(), key=lambda pair:pair[1]) for word in words}


print(max(repeated_vowels(words).items(), key=lambda w: w in vowels))