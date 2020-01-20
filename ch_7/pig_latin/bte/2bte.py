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

# Assume that you have a list of dicts, in which each dict contains two name-value pairs: "name" and "hobbies," 
# where "name" is the person’s name, and "hobbies" is a set of strings representing the person’s hobbies. What are the three most popular hobbies among the people listed here?

person = [
    {'name': 'Jim', 'hobbies': 'read cook sing'},
    {'name': 'Sam', 'hobbies': 'cook play garden'},
    {'name': 'George', 'hobbies': 'cook swim garden'}
]



all_hobbies = {}
for each_indiv in person:
    for hobby in each_indiv['hobbies'].split(" "):
        print(hobby)
#     for hobby in each_indiv['hobbies']:
#         # print(hobby)
#         all_hobbies[hobby].get(hobby, 0) + 1
# print(all_hobbies)

