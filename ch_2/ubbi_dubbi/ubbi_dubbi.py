word = "soap"


def translate(word):
    new_word = ""
    for letter in word:
        if letter not in "aeiou":
            new_word += letter
        else:
            new_word += "ub" + letter
    return new_word.capitalize() if word.istitle() else new_word
