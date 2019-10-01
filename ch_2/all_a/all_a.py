mylist = list(range(10))

# One solution
new_list = []
for item in mylist[:7]:
    new_list.append("a")


# Second solution
new_list = []
for i, item in enumerate(mylist):
    if i <= 5:
        new_list[i : i + 1] = "a"
print(new_list)
