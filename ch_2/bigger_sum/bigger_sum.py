

#Write a function, mysum_bigger_than, that takes a first argument, preceding \*args. 
# That argument indicates the threshold for including an argument in the sum. 
# Thus, calling mysum_bigger_than(10, 5, 20, 30, 6) would return 50 — because 5 and 6 aren’t greater than 10. 
# This function should similarly work with any types, and assumes that all of the arguments are of the same type.  

def mysum_bigger_than(arg1, *args):
    threshold = arg1
    total = type(args[0])()

    for items in args:
        if items >= threshold:
            total += items

    return total

# print(mysum_bigger_than(10, 5, 20, 30, 6))

# print(mysum_bigger_than('ttt', 'bbb', 'xxw'))

