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



student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
# sorted(student_tuples, key=lambda student: student[2])   # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# print(sorted(people, key=lambda lastname: lastname[1]))

new = {
    'person1': ['Reuven', 'Lerner', 'reuven@lerner.co.il'],
    'person2': ['Donald', 'Trump', 'president@whitehouse.gov'],
}

person1 = ['Reuven', 'Lerner', 'reuven@lerner.co.il']

