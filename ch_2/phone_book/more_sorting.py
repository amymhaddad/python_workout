from operator import itemgetter
import collections

# Problem 1: Given a sequence of positive and negative numbers, sort them by absolute value
numbers = [1, 2, -1, 0, -4.5, 6]
print(sorted(numbers, key=lambda x: abs(x)))


# Problem 2: Given a list of strings, sort them according to how many vowels they contain.
words = ["you", "me", "elephant", "sync"]


def count_vowels(words):
    vowel_count = {}

    vowels = "aeiou"
    counter = 0

    for word in words:
        vowel_count[word] = 0
        for letter in word:
            if letter in vowels:
                vowel_count[word] += 1

    return vowel_count


sorted_words = [
    word[0] for word in sorted(count_vowels(words).items(), key=lambda v: v[1])
]


# Problem 3: Given a list of lists, with each list containing zero or more numbers, sort by the sum of each inner list’s numbers.

numbers = [[2, 2], [1, 2], [1, 2, 3]]

summed_nums = [[sum(num)] for num in numbers]
zipped = zip(numbers, summed_nums)
new_list_numbers = [number[0] for number in sorted(zipped, key=lambda x: x[1])]

print(new_list_numbers)
