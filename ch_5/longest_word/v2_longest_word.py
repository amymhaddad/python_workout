import os

directory_name = "./books"


def longest_word(filename):

    longest_word = ""
    for line in open(filename):
        for word in line.split():
            if len(word) > len(longest_word):
                longest_word = word
    return longest_word


find_longest_word = {
    filename: longest_word(os.path.join(directory_name, filename))
    for filename in os.listdir(directory_name)
    if os.path.isdir(directory_name)
}
