# Read through a text file on disk. Use a dict to track how many words of each length are in the file —
# that is, how many 3-letter words, 4-letter words, 5-letter words, and so forth. Display your results.

from string import punctuation


def read_in_text(file):
    """Return a list of words from a text file without puncuation or extra spaces"""

    with open(file) as file_object:
        lines = file_object.readline()

    word_list = []
    for word in lines.split(" "):
        if word[-1] in punctuation or "\n" in word:
            remove_space = word.replace("\n", "")
            word_list.append(remove_space.strip(punctuation))
        else:
            word_list.append(word)
    return word_list


# Option 1: use .get()
def count_words(word_list):
    """Return a dictionary to track the number of words 
    for each length from the file (ie, 15 5-letter words)"""

    word_count = {}

    for word in word_list:
        word_count[len(word)] = word_count.get(len(word), 0) + 1
    return word_count


print(count_words(read_in_text("text_file.txt")))
# result: {5: 15, 3: 5, 4: 13, 11: 6, 10: 3, 8: 5, 6: 4, 7: 7, 9: 1, 2: 1} --> ie, 15 5-letter words, 5 3-letter words...

# Option 2: use defaultdict()
from collections import defaultdict


def count_words(word_list):
    """Return a dictionary to track the number of words 
    for each length from the file (ie, 15 5-letter words)"""

    word_count = defaultdict(int)

    for word in word_list:
        if len(word) not in word_count.keys():
            word_count[len(word)] = 1
        else:
            word_count[len(word)] += 1

    return word_count


print(count_words(read_in_text("text_file.txt")))
# Result: defaultdict(<class 'int'>, {5: 15, 3: 5, 4: 13, 11: 6, 10: 3, 8: 5, 6: 4, 7: 7, 9: 1, 2: 1})
