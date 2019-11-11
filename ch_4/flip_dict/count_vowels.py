# Given a string containing several (space-separated) words, 
# create a dict in which the keys are the words, and the values are the number of vowels in each word. 
# If the string is 'this is an easy test', then the resulting dict would be {'this':1, 'is':1, 'an':1, 'easy':2, 'test':1}.

string = "this is an easy test"
vowels = "aeiou"

dict = {}
counter = 0
for word in string.split(" "):
    for letter in word:
        if letter in vowels:
            counter+= 1

    dict[word] = counter
    counter = 0

# print(dict)



