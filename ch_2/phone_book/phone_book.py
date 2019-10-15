people = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
 {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
 {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}
 ]

import operator


combined = {}

for person in people:
    for attribute, details in person.items():
        if attribute not in combined:
            combined[attribute] = [details]
        else:
            combined[attribute].append(details)



last_names = ['Lerner', 'Trump', 'Putin']

new_name = []

for i in range(1, len(last_names)+1):
    print(last_names[i])
    # if last_names[i] < last_names[:i+1]:
    #     new_name.append(name[i])
    # index += 1


print(new_name)

    # if operator.lt(name, name[i]):
    #     new_name.append(name)






# {'first': ['Reuven', 'Donald', 'Vladimir'], 'last': ['Lerner', 'Trump', 'Putin'], 'email': ['reuven@lerner.co.il', 'president@whitehouse.gov', 'president@kremvax.ru']}


# last_names = ''
# for person in people:
#     for attribute, detail in person.items():
#         import pdb; pdb.set_trace()
#         if attribute == 'last' and operator.gt(detail, person['last'] ):
            
        
#             print(detail)
















# last_names = []

# for person in people:
#     # for category, details in person.items()
#     for cateogory, details in person.items():
#         if cateogory == 'last':
#             last_names.append(details)

# sorted_last_names = sorted(last_names)



        
