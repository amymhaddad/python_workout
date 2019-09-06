user_name = input("Enter your name: ")

# Use for loop without enumerate
name_triangle = ""
increment = 1
for letter in user_name:
    name_triangle += user_name[0:increment] + "\n"
    increment += 1
print(name_triangle)

# Use for loop with enumerate
for i, letter in enumerate(user_name):
    name_triangle += user_name[0 : i + 1] + "\n"
print(name_triangle)
