from collections import Counter


words = ["this", "is", "a", "test", "program"]


def count_words_with_repeat_letters(words):
    """Return a dictionary that contains each word 
    and the number of repeated letters it contains"""

    repeats = {}
    counts = []

    for word in words:
        for letter in word:
            counter = word.count(letter)
            counts.append(counter)
            repeats[word] = max(counts)
        counts = []
    return repeats


def most_repeating_word(repeats):
    """Return the words with the most repeated letters"""

    max_count = [count for count in repeats.values()]

    most_repeating = [
        word for word, count in repeats.items() if count == max(max_count)
    ]

    return "\n".join(most_repeating)


print(most_repeating_word(count_words_with_repeat_letters(words)))
