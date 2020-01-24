# Given a text file, what are the lengths of the different words? Return a set of different word lengths in the file.


word_lengths = {len(word) for word in open("words.txt").readlines()}

print(word_lengths)
