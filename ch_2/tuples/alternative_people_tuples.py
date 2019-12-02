people = [
    ("Donald", "Trump", 7.85),
    ("Vladimir", "Putin", 3.626),
    ("Jinping", "Xi", 10.603),
]

import operator
#use a for loop to cycle through the list of tuples; use sorted() with a key that's set to itemgetter(1,0)
#itemgetter(1,0) will sort the tuple by the first element, then the second
# for person in sorted(people, key=operator.itemgetter(1, 0)):
    #each person is tuple
    #use .format() to extract the elements AND add padding beteween them
    #{1:10} --> the 1 means the first element; 10 here means 10-field space 
    #{2:5.2f} -->{2nd_element: 5_spaces.round_by_2}
    #pass in *persons --> *person, when passed to a function, becomes not a tuple, but the elements of that tuple. That is, 3 separate argumenst 

    # print("{1:10} {0:10} {2:5.2f}".format(*person))




# for person in sorted(people, key=operator.itemgetter(1, 0)):
#     print("{1:10} {0:10} {2:5.2f}".format(*person)




def important_people(people):
    all_people = ""
    for person in people:
        all_people += "{0:10} {1:10} {2:5.2f}\n".format(*person)

    return all_people.strip()

print(important_people(people))



#Notes:
#IF you have a function that takes three params, and you pass three args -- you get a 1:1 match
#BUT if you want to pass a tuple of 3 elements (or a list of 3 elemetns) to a function that takes 3 params, it won't work! 
# You need to use a splat (*) in the function invocation -- that is, when you call the function. 
#This turns the tuple (ie, iterable) into multiple arguments. Instead, you're passing not a tuple, but 3 args 


#sort() only works on a list (and sorts in place)
#sorted() takes in an iterable, then checks the first element, then the second, and the third....
#sorted() with key= //// and set key= to a function 

#function takes in a tuple and returns the last name. THEN, apply this function to key=, so when sort() is called, the names are sorted by last name 
#return t[1] AND t[0] incase there are people with the same last name
# def by_last_name(t):
#     return t[1], t[0]

# for person in sorted(people, key=by_last_name):
#     print("{0:10} {1:10} {2:5.2f}".format(person[1], person[0], person[2]))


#BUT when you use a oneline function, you can use a lambda
#Here, each tuple is passed to the key (the lambda function). That function will return a value, and that's the value that'll be used in the sorting 
# for person in sorted(people, key=lambda t: (t[1][0])):
#     print("{0:10} {1:10} {2:5.2f}".format(person[1], person[0], person[2]))


# for person in sorted(people, key=operator.itemgetter(1, 0), reverse=True):
#     print("{1:10} {0:10} {2:5.2f}".format(person[1], person[0], person[2]))



def by_last_name(t):
    return t[1]

for person in sorted(people, key=by_last_name):
    print("{0:10} {1:10} {2:5.2f}".format(*person))

for person in sorted(people, key=lambda t:t[1][0]):
    print("{0:10} {1:10} {2:5.2f}".format(*person))


# for person in sorted(people, key=lambda t: (t[1][0])):
#     print("{0:10} {1:10} {2:5.2f}".format(person[1], person[0], person[2]))