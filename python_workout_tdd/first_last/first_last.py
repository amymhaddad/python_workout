
#Option 1
def firstlast(arg):

    if isinstance(arg, str):
        return arg[0] + arg[-1]
    elif isinstance(arg, list):
        return [arg[0], arg[-1]]
    else:
        return (arg[0], arg[-1])

#Option 2
def firstlast(arg):
    return arg[0] + arg[-1]


print(firstlast((1, 2, 3, 4)))
