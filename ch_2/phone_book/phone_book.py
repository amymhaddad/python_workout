people = [
    {"first": "Reuven", "last": "Lerner", "email": "reuven@lerner.co.il"},
    {"first": "Donald", "last": "Trump", "email": "president@whitehouse.gov"},
    {"first": "Vladimir", "last": "Putin", "email": "president@kremvax.ru"},
]


def update_people(people):
    """Put a dictionary into a list"""
    updated_list = []
    for person in people:
        attribute = sorted(person, reverse=True)
        for item in attribute:
            updated_list.append(person[item])
    return updated_list


people_list = update_people(people)


def alpha_order(people_list):
    """Put a given list in alphabetical order: Lastname, Firstname, Email"""

    index = 0
    final = []
    for person in people_list:
        final.append(people_list[index : index + 3])
        index += 3
        if index >= len(people_list):
            return final
            break


for person in alpha_order(people_list):
    print(" ".join(person))
