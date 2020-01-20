import re


words = "text.txt"

def parse_data(words):
    return [  
        re.sub(r'[\W+]',"", words).lower()
        for lines in open(words)
        for words in lines.split(" ")     
    ]


def pig_latin(list_of_words):

    return "".join(
        word +"way " 
        if word[0] in "aeiou"
        else word[1:] + word[0] + "ay" + " "
        for word in parse_data(words)
    )
    
print(pig_latin(words))

