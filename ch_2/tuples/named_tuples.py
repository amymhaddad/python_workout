# Exerice 1: Use namedtuple and write a Python program that takes the people list (below), and produces a table.
from collections import namedtuple

people = [
    ("Donald", "Trump", 7.85),
    ("Vladimir", "Putin", 3.626),
    ("Jinping", "Xi", 10.603),
]

Person = namedtuple("Person", ["last", "first", "time"])


def table_of_peope(people):

    update = ""
    for person in people:
        update += "{0:10} {1:10} {2:5.2f}\n".format(*Person._make(person))
    return update.strip()


# print(table_of_peope(people))

# Exercise 2: Define a list of tuples, in which each tuple contains the name, length (in minutes), and director of the movies nominated for "best picture" Oscar awards last year.
# Ask the user whether they want to sort the list by title, length, or director’s name,
# and then present the list sorted by the user’s choice of axis.
# The user can input 1, 2, or 3 fields to sort by.

import operator

movies = [
    ("Winter in Boston", 120, "Jill McFee"),
    ("Adventures of P&A", 147, "Arnold Masters"),
    ("Move to Florida", 90, "George Bee"),
]

Movie = namedtuple("Movie", ["title", "length", "director"])

print("Sort the movies by title, length or director. You can sort one or all fields.")
print()
user_sort = input(
    "Enter the field(s) you want to sort by, with each field separated by a comma: "
)


def movie_dictionary(movies):
    """Return a dictionary of movie namedtuples"""

    all_movies = []
    for movie in movies:
        each_movie = Movie(*movie)
        all_movies.append(each_movie._asdict())
    return all_movies


def sort_movie_output(user_sort):
    """Sort movies based on user input"""
    fields = [info for info in user_sort.split(", ")]
    user_preferences = ""
    for movie in sorted(movie_dictionary(movies), key=operator.itemgetter(*fields)):
        user_preferences += "{title:10} {length:10} {director:5} \n".format(**movie)
    return user_preferences.strip()


print(sort_movie_output(user_sort))
