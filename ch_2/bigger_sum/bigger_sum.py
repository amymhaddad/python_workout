




def mysum_bigger_than(arg1, *args):

    threshold = arg1
    total = type(args[0])()

    for items in args:
        
        if isinstance(total, int):
            
            if items >= threshold:
                # import pdb; pdb.set_trace()
                total += items
        # else:

    return total

print(mysum_bigger_than(10, 5, 20, 30, 6))

# print(mysum_bigger_than('azz', 'bbb', 'ccc'))