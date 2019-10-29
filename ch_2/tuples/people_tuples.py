people = [
    ("Donald", "Trump", 7.85),
    ("Vladimir", "Putin", 3.626),
    ("Jinping", "Xi", 10.603),
]


def important_people(people):
    all_people = ""
    for person in people:
        rounded_number = "{:.2f}".format(person[2])
        all_people += "{0:10} {1:10} {2:5}\n".format(
            person[1], person[0], rounded_number
        )

    return all_people.strip()


print(important_people(people))
