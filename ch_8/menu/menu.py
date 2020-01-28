


#  If the user enters a string that matches one of the keywords arguments, then the function associated with that keyword will be invoked, 
#  and its return value will be returned to `menu’s caller. If the user enters a string that is not one of the keyword arguments, then the user will be given an error message, and asked to try again.




def func_a():
    return "A"

def func_b():
    return "B"



def menu(**options):
    while True:
        #join together all of the options passed in
        option_string = '/'.join(sorted(options))


        choice = input(f"Enter an option ({option_string}): ")
        if choice in options:
            return options[choice]()
        else:
            print("Not a valid option")


#kwargs sets a key to a value
return_value = menu(a=func_a, b=func_b)
print(f'Result is {return_value}')