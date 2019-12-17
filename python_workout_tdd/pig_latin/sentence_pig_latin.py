# Ex 1: Translate a series of English words into Pig Latin.
def convert_sentence(sentence):

    translated_sentence = []

    for word in sentence.split(" "):
        if word.startswith(("a", "e", "i", "o", "u")):
            translated_sentence.append(word + "way")
        else:
            translated_sentence.append(word[1:] + word[0] + "ay")

    return " ".join(translated_sentence)

    sentence = input("Enter a sentence: ")


# Ex 2: Take a text file, creating (and printing) a nonsensical sentence from the nth word on each of the first 10 lines, where n is the line number.
import re


def nonsense():
    with open("text.txt") as f_object:
        rows = f_object.readlines()

    nonsense_sentence = ""
    for i, row in enumerate(rows):
        word = row.split(" ")[i]
        validate_word = re.sub(r"\W+", "", word) + " "
        nonsense_sentence += validate_word

    return nonsense_sentence


print(nonsense())
