# Define a dictionary in which the keys are names of children in a family, and the values are lists of strings representing the grandchildren.
# That is, the dict {'A':['B', 'C', 'D'], 'E':['F', 'G']} means that A and E are siblings, and that A’s children are B, C, and D, while E’s children are F and G. Using a list comprehension, produce a list of the grandchildren.


family = {"A": ["B", "C", "D"], "E": ["F", "G"]}

grandkids = [grandkid for kid, grandkids in family.items() for grandkid in grandkids]
print(grandkids)
