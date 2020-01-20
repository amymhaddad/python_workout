#Write a new function, "funcfile", that will take two arguments — a filename and a function. 
# The output from the function should be a string, the result of invoking the function on each word in the text file. 



def uppercase_letters(word):
    return word.upper()


def convert_words(file, func):

    with open(file) as text_file:
        convert =  "".join([
        uppercase_letters(word)
        for words in text_file.readlines()
        for word in words
    ])
    text_file.close()
    return convert

print(convert_words("text.txt", uppercase_letters))
