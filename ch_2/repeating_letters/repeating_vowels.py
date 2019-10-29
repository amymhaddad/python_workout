
from collections import Counter
import operator

words = ['ttttttttttest', 'program', 'iiiiis']
vowels = "aeiou"



#need to get a conditional in here somehow to only count the letters with vowels    
repeated_vowels = { word: max(Counter(word).items(), key=lambda pair:pair[1]) for word in words}

print(max(repeated_vowels, key=lambda w:repeated_vowels[w][0] in vowels))


def most_repeating_letter_count(word):
    for letter in word:
        return Counter(word).most_common()


def most_vowels(words):
    repeats = { word: most_repeating_letter_count(word) for word in words}
    # print(repeats)

    return max(repeats, key=lambda x: x in vowels)

# print(most_vowels(words))

# return max(word_counts.items(), key=operator.itemgetter(1))[0]