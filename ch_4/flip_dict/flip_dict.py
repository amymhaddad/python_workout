d = {'a':1, 'b':2, 'c':3}

#Option 1
flipped_dict = { id: name for name, id in d.items() }
# print(flipped_dict)

#Option 2
flipped_dict2 = {}
for name, id in d.items():
    flipped_dict2[id] = name
print(flipped_dict2)

#Option 3
flipped_dict3 = { d[key]: key for key in d }
