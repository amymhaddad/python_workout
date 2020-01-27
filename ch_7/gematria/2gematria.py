# In this exercise, you will write two functions:

# gematria_for, which takes a single word (string) as an argument, and returns the gematria score for that word
# gematria_equal_words, which takes a single word and returns a list of those dictionary words whose gematria score matches the current word’s score.
# For example, if the function is called with the word cat, with a gematria value of 24 (3 + 1 + 20), then the function will return a list of strings, all of whose gematria is also 24.


from string import ascii_lowercase as letters


gematria = {letter: number for number, letter in enumerate(letters, 1)}


def gematria_for(word):
    return sum(gematria.get(letter, 0) for letter in word)


def gematria_equal_words(single_word):

    return [
        word.strip().lower()
        for word in open("words.txt")
        if gematria_for(word.strip().lower()) == gematria_for(single_word)
    ]
