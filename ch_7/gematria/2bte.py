# Create a list of tuples in which each tuple contains three elements:
# (1) the author’s first and last names, (2) the book’s title, and (3) the book’s price in US dollars.
# Use a dict comprehension to turn this into a dictionary whose keys are the book’s titles, with the values being another (sub-) dictionary, with keys for (a) the author’s first name, (b) the author’s last name, and (c) the book’s price in US dollars.

authors = [
    ("Amy Haddad", "How to Be a Great Programmer", 25),
    ("Jim Beam", "How to Be a Farmer", 20),
    ("Jo Smo", "How to Program", 30),
]


author_book = {}
for author in authors:
    author_book[author[1]] = {
        "first_name": author[0].split()[0],
        "last_name": author[0].split()[1],
        "price": author[2],
    }

print(author_book)
