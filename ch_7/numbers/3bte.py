# Define a list of five dictionaries. Each dict will have two key-value pairs, "name" and "age", 
# containing a person’s name and age (in years). 
# Use a list comprehension to produce a list of dicts in which each dict contains three key-value pairs — the original "name" and "age", and a third "age_in_months" key, containing the person’s age in months. 
# However, the output should exclude any of the input dicts representing people above 20 years of age.


people_ages = [
    {'name': 'Amy', 'age': 12}, 
    {'name': 'Henry', 'age': 30}, 
    {'name': 'Zack', 'age': 70}, 
    {'name': 'Sam', 'age': 2}, 
    {'name': 'Jim', 'age': 40}, 
]


# {x : 2*x for x in range(5)]

people_under_twenty = [
    # person
    # for person in people_ages
    # person.update(age_in_months = person['age'] * 12)
    persons.update(age_in_months = persons['age'] * 12)
    # persons.setdefault("age_in_months", persons['age'] * 12 )
     
    for persons in people_ages
   
]
 
print(people_under_twenty)



#use setdefault
# for person in people_ages:
#     person.setdefault("age_in_months", person['age'] * 12 )
#     if person['age'] < 20:
#         print(person)


# for person in people_ages:
#     person["age_in_months"] = person['age'] * 12
#     if person['age'] < 20:
#         print(person)


