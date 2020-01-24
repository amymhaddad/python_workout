conversion = {"euro": 0.91, "ruble": 62.67, "yen": 108.94}


user_input = input("Enter a currency you'd like to convert to US dollars: ")

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


for details in author_book.values():
    country_conversion = details["price"] * conversion[user_input]

    details["price"] = "{:.2f}".format(country_conversion)

print(author_book)
