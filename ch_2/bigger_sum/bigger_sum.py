




def mysum_bigger_than(arg1, *args):

    threshold = arg1
    total = type(args[0])()

    for item in args:
        if item >= threshold:
            # import pdb; pdb.set_trace()
            total += item
    return total

print(mysum_bigger_than(10, 5, 20, 30, 6))