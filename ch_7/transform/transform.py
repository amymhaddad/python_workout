d = {"a": 1, "b": 2, "c": 3}

# Option 1
# def transform_values(v):

#     new_dict = {
#        k: v * v
#         for k, v in d.items()
#     }

#     return new_dict


# Option 2
def transform_values(funct, d):
    return {letter: funct(number) for letter, number in d.items()}


print(transform_values(lambda x: x * x, d))
