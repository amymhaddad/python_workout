
#Exercise 1
def mysum_bigger_than(arg1, *args):
    threshold = arg1
    total = type(args[0])()

    for items in args:
        if items >= threshold:
            total += items

    return total

# print(mysum_bigger_than(10, 5, 20, 30, 6))

# print(mysum_bigger_than('ttt', 'bbb', 'xxw'))


#Exercise 2:
from string import digits

def sum_numeric(*args):

    total = 0
    for item in args:
        if isinstance(item, int):
            total += item
        elif item in digits:
            total += int(item)
    return total

# print(sum_numeric(10, 20, 'a', '30', 'bcd'))



#Exercise 3:

people = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
 {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
 {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}
 ]

def combine_people(persons):
    attributes = persons[0].keys()
    
    combined = {}

    #this for loop creates a new list for each key
    for key in attributes:
        combined[key] = []

    for person in persons:
        
        for attribute, value in person.items():
            combined[attribute].append(value)

    return combined
        

# print(combine_people(people))



def single_dictionary(people):

    single_dict = {}
    person_details = []

    for person in people:
        
        for key, value in person.items():
            
            if key not in single_dict.keys():
                #this syntax creates a new list [] in memory each time through the loop 
                single_dict[key] = [value]                
            else:
                single_dict[key].append(value)

        

    return single_dict
        
print(single_dictionary(people))


# {'first': ['Reuven', 'Lerner', 'reuven@lerner.co.il', 'Donald', 'Trump', 'president@whitehouse.gov', 'Vladimir', 'Putin', 'president@kremvax.ru'], 'last': ['Reuven', 'Lerner', 'reuven@lerner.co.il', 'Donald', 'Trump', 'president@whitehouse.gov', 'Vladimir', 'Putin', 'president@kremvax.ru'], 'email': ['Reuven', 'Lerner', 'reuven@lerner.co.il', 'Donald', 'Trump', 'president@whitehouse.gov', 'Vladimir', 'Putin', 'president@kremvax.ru']}
# bigger_sum bigger_sum %




# person_details = []

# single_dict = {}
# people = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'}, {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},]

# for person in people:
#     for key, value in person.items():
#         if key not in single_dict.keys():
#             single_dict[key] = [value]

#         else:
#             # import pdb; pdb.set_trace()
#             print(key)

#             print(single_dict[key] + [value])
#             # single_dict[key] + [value]
#             # print(single_dict)

            
#                 # single_dict.value + value
#             # print(single_dictionary[key])

            
# print(single_dict)