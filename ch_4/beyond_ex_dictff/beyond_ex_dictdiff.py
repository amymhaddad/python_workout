# Exericse 1:
# d1 = {'d': 1, 'e': 3, 'g': 5}
# d2 = {'d': 2, 'e': 4, 'h': 6 }
# d3 = {'d': 5}

# first iteration of ex 1 - function takes in 2 dictionaries
def update_dict(d1, d2):
    all_keys = set(d1) & set(d2)
    all_values = set(d1.values())

    for key in all_keys:
        if key in d1 and key in d2:
            d1.update(d2)
    return d1


# exercise 2
def even_odd_dictionary(*args):
    new_dict = {}

    for i, item in enumerate(args):
        if i % 2 == 0:
            continue
        else:
            new_dict[args[i - 1]] = item
    return new_dict


# print(even_odd_dictionary('a', 1, 'b', 2))

# exercise 3

dict = {"a": 1, "b": 2, "c": 3, "d": 4}


def f(k, v):
    for i, pair in enumerate(dict):
        if k == pair:
            return bool(i % 2 == 0)


def dict_partition(dict, f):
    d1 = {}
    d2 = {}

    for k, v in dict.items():
        if f(k, v):
            d1[k] = dict.get(k)
        else:
            d2[k] = dict.get(k)
    return d1, d2


# print(dict_partition(dict, f))
