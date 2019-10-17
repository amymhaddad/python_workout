people = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
 {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
 {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}
]

import operator



updated_list = []

for person in people:
    attribute = sorted(person, reverse=True)
    for item in attribute:
        updated_list += [person[item]]
    
print(updated_list)


# student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10),
# ]
# # sorted(student_tuples, key=lambda student: student[2])   # sort by age
# # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# # print(sorted(people, key=lambda lastname: lastname[1]))

new = [
    ['Lerner', 'Reuven', 'reuven@lerner.co.il'],
    ['Trump', 'Donald', 'president@whitehouse.gov'],
    ['Putin', 'Vladimir', 'president@kremvax.ru'],
]

# x = sorted(new, key=lambda x:x[1])

# for person in x:
#     print(" ".join(person))





