
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


def single_dictionary(people):

    single_dictionary = {}
    
    for person in people:
        for key, value in person.items():
            # single_dictionary.get(key, value)
            # single_dictionary[key] = value
    return single_dictionary
        
print(single_dictionary(people))


    # for key, value in person.items():
    #     # print(key, value)
    #     new_dictionary['key'] = value
        
