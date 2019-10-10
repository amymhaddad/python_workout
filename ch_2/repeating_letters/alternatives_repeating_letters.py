from collections import Counter
import operator

words = ['this', 'is', 'a', 'test', 'program']

def most_repeating_letter_count(word):
    #the syntax [0][1] indexes into the sorted dictionary to grab the repeated number itself
    ##Return the number of times the most frequently appearing letter is in the word  // we’re only interested in the highest-scoring letter
    return Counter(word).most_common(1)[0][1]


def most_repeating_word(words):
    #create a dictionary comprehension, word_counts, and set the "word" as the key and the value as the function above 
    #the keys are our words and whose values are the results from invoking most_repeating_letter_count on each word.
    #Ultimately, word_counts is a dictionary with the words and the number of repeated letters for each word
    word_counts = {word : most_repeating_letter_count(word)
                   for word in words}
  
    #return the largest count, using itemgetter.  
    #itemgetter syntax: pass in the key you want to get the value; use [0] to index into the tuple and get a string
    #For this ex, I get the max number from the dictionary above, and use itemgetter(1) to extract the word with the largest repeated number count

    return max(word_counts.items(), key=operator.itemgetter(1))[0]

# print(most_repeating_word(words))


#examine problem

#returns a list of tuples
# x = [Counter(word).items() for word in words]

#From a list comp to a dictionary comp that uses max
# print(max(Counter(word).items() for word in words))
# dict_items([('t', 1), ('h', 1), ('i', 1), ('s', 1)])

#Dict comp that uses key= to find the most commonly used letter
#Add the key= to max (ie, max(iterable, key=function)) in order to apply max to a list of tuples  (see above)
#Add a lambda to the key to look at each tuple and apply max() to each one
#key=lambda pair: pair[1] gives us a pair (ie, a tuple: ('t', 1) ); use index [1] to get the number (ie, the value)

from collections import Counter
import operator

words = ['this', 'is', 'a', 'test', 'program']

#Dictionary comprehension 
#max( key=) -->key= lets me apply a function to each element in max()
#{word (ie, key): max(Counter(word).items() (ie, value), key=lambda pair:pair[1] for word in words }

#max(Counter(word).items() --> gets the letter count for each word. Notice that I pass in "word" to the counter. note:.items() gives me the letter and count associated with each word

letter_counter = {word: max(Counter(word).items(), key=lambda pair: pair[1]) for word in words}
# {'this': ('t', 1), 'is': ('i', 1), 'a': ('a', 1), 'test': ('t', 2), 'program': ('r', 2)}


#when use max, min, or sort() on a dictionary, we get back the dictionary's keys
#key=lambda w:letter_counter[w] will give me back the tuple. SO, w (ie, word) indexes into dictionary and gives me the tuple associated with the word. 
#And I want the count inside that tuple
print(max(letter_counter, key=lambda w:letter_counter[w][1]))


### 
# words2 = "This is a bunch of words for my Python book exercise on repeated words"
# split_words = words2.split()
# word_count2 = { word: max(Counter(word).items(), key=lambda pair: pair[1]) for word in split_words}

# print(max(word_count2, key=lambda w: word_count2[w][1]))


words2 = "Thiiiiis is a word".split()
# words2_count = { word: max(Counter(word).items(), key=lambda p: p[1]) for word in words2 }

# print(words2_count)

word_letter_count = {}
for word in words2:
    word_letter_count[word] = max(Counter(word).items(), key=lambda p: p[1])
# print(word_letter_count)
#Result: {'Thiiiiis': ('i', 5), 'is': ('i', 1), 'a': ('a', 1), 'word': ('w', 1)}

#from the dictionary of --> words: (letter, count):
#max(dictionary, function) -->apply the function to the dictionary (ie, look at the counts and give the max count)
# print(max(word_letter_count, key=lambda w: word_letter_count[w][1]))




#EXTRA info:
#Counter and Counter.most_common()
#Counter(iterable)
#Counter(iterable).most_common(number) --> insert the number to return a list of the 'n' most common elements and their counts, from most to least common
##EX: Counter('abracadabra').most_common(3) -->return a list of 3 elements 
#Feed Counter a word, and it’ll tell us how many times each letter appears in that word; use Counter.most_common() to see how often our iterable appears


#ie, print(Counter('aaaabbbccc').most_common(2)) ---> get the 2 most common elements
#print(Counter('aaaabbbccc').most_common(1)) --->get 1 most common element
#IF I don't pass in an argument, then the sorted dictionary is returned from most common the least common elements.
# print(Counter('aaaabbbccc').most_common(2))


#Counter("ababa").items()
# >>> get a tuple


#max() --> use "key=" in max 



# people = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
#  {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
#  {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}
#  ]

#itemgetter ex: 
#I wnat to get the VALUES associated with 'last', 'first'
# # import operator
# for person in sorted(people, key=operator.itemgetter('last', 'first')):
#     print(f"{person['last']}, {person['first']}: {person['email']}")