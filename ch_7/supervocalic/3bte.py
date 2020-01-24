# Create a list whose elements are strings — the names of people in your fanily.
# Now use a set comprehension (and better yet: a nested set comprehension) to find which letters are used in your family members' names.


names = ["Suzy", "James", "William", "Peter", "Samantha"]

letters = {letter.lower() for name in names for letter in name}

print(letters)
