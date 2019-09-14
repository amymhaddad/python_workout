sentence = "this is a test translation"
new_sentence = ""

for word in sentence.split(" "):

    if word[0] in "aieiou":
        new_sentence += word + "way" + " "
    else:
        new_sentence += word[1:] + word[0] + "ay" + " "

print(new_sentence)
