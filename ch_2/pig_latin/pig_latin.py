user_word = input("Enter a word: ")

# One solution to the problem
def translate_word(user_word):

    new_word = user_word
    vowels = ["a", "e", "i", "o", "u"]

    if new_word[0] in vowels:
        new_word += "way"
        return new_word
    else:
        first_letter = new_word[0]
        new_word += first_letter
        return new_word.replace(new_word[:2], "ay")


print(translate_word(user_word))

# A second solution to the problem
def translate_word(user_word):

    new_word = user_word
    vowels = ["a", "e", "i", "o", "u"]

    word_as_list = [letter for letter in user_word]
    first_letter = word_as_list[0]

    for letter in word_as_list:
        if first_letter in vowels:
            word_as_list.append("way")
            return "".join(word_as_list)
        else:
            word_as_list.remove(first_letter)
            word_as_list.append(first_letter + "ay")
        return "".join(word_as_list)


print(translate_word(user_word))
