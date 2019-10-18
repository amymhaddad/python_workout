
from operator import itemgetter
import collections

#Given a sequence of positive and negative numbers, sort them by absolute value
numbers = [1, 2, -1, 0, -4.5, 6]
print(sorted(numbers, key=lambda x: abs(x)))

#Given a list of strings, sort them according to how many vowels they contain.
words = ['you', 'me', 'elephant', 'sync']

def count_vowels(words):
    vowel_count = {}

    vowels = 'aeiou'
    counter = 0

    for word in words:
        vowel_count[word] = 0
        for letter in word:
            if letter in vowels:
                vowel_count[word] += 1
        
    return vowel_count

print(count_vowels(words))


#sort the ITEMS of the dictionary; index into each dictionary to get the value with this syntax-->  key=lambda v: v[1]
print(sorted(count_vowels(words).items(), key=lambda v: v[1]))

for word in sorted(count_vowels(words).items(), key=lambda v: v[1]):
    print(word[0])

#use orderedDict when you want to return an instance of a dict subclass, supporting the usual dict methods. 
# An OrderedDict is a dict that remembers the order that keys were first inserted.
# print(collections.Counter(vowel_count))