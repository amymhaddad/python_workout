def secret_word(word):
    if word.startswith(("a", "e", "i", "o", "u")):
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"


word = input("Enter a word: ")
