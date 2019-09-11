import string

PUNCTUATION = string.punctuation
user_word = input("Enter a word: ")


def starts_with_vowel(user_word):
    """Add 'way' to end of word. Capitalize the returned word if the user_word is capitalized"""
    styled_word = user_word

    if user_word[0].isupper():
        return styled_word.capitalize() + "way"
    return styled_word + "way"


def starts_with_constant(user_word):
    """Move the first letter of the word to the end of the user word and add 'ay'.
    Capitalize the returned word if the user_word is capitalized."""

    styled_word = f"{user_word[1:]}{user_word[0]}{'ay'}"

    if user_word.islower():
        return styled_word
    return styled_word.capitalize()


def has_punctuation(pig_latin_word):
    """Put the punctuation mark at the end of the word"""

    styled_word = pig_latin_word

    for char in styled_word:

        if char in PUNCTUATION:
            styled_word = styled_word.replace(char, "")
            styled_word += char
            return styled_word

    return styled_word


def translate_to_pig_latin(user_word):
    """Create a new pig latin word"""

    if user_word[0] in "aeiouAEIOU":
        new_word = starts_with_vowel(user_word)
    else:
        new_word = starts_with_constant(user_word)

    for letter in new_word:
        if letter in PUNCTUATION:
            return has_punctuation(new_word)
    return has_punctuation(new_word)


print(translate_to_pig_latin(user_word))
