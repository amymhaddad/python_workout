#Exercise 1:
#Use a nested list comprehension to transform a list of dictionaries into a list of 2-element (name-value) tuples, 
# each of which represents one of the name-value pairs in one of the dictionaries. If more than one dictionary has the same name-value pair, then the tuple should appear twice.


people = [
    {"name": "Amy"},
    {"name": "Sam"},
    {"name": "Bob"}    
]

tup = (
    (category, name)
    for person in people
    for category, name in person.items()
)

# print(next(tup))


#Exercise 2:
# Assume that you have a list of dicts, in which each dict contains two name-value pairs: "name" and "hobbies," 
# where "name" is the person’s name, and "hobbies" is a set of strings representing the person’s hobbies. What are the three most popular hobbies among the people listed here?

person = [
    {'name': 'Jim', 'hobbies': 'read cook sing'},
    {'name': 'Sam', 'hobbies': 'cook play garden'},
    {'name': 'George', 'hobbies': 'cook swim garden'}
]


count = 0
fav_hobbies = {}
all_hobbies = [
    {hobby: each_indiv.get(hobby, 0) + 1}
    for each_indiv in person
    for hobby in each_indiv['hobbies'].split(" ")   
]

print(all_hobbies)
# >>>
# [{'read': 1}, {'cook': 1}, {'sing': 1}, {'cook': 1}, {'play': 1}, {'garden': 1}, {'cook': 1}, {'swim': 1}, {'garden': 1}]]

#for loop option:
all_hobbies = {}
for each_indiv in person:
    for hobby in each_indiv['hobbies'].split(" "):
        all_hobbies[hobby] = all_hobbies.get(hobby, 0) + 1

print(sorted(all_hobbies.items(), key=lambda x: x[1], reverse=True)[:3])
# >>>
# [('cook', 3), ('garden', 2), ('read', 1)]


