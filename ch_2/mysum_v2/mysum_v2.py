arg1 = "abc"
arg2 = "def"
arg3 = "ddd"

# Concatentate a specific number of arguments of the same type
def firstlast(arg1, arg2):
    return arg1 + arg2


# Concatentate an unlimited number of arguments of the same type; algorithm with input from book's solution
def firstlast(*args):
    if not args:
        return args
    update_sequence = args[0]

    for item in args[1:]:
        update_sequence += item
    return update_sequence


print(firstlast(arg1, arg2, arg3))
