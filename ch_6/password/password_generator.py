import random

# create an outer function that takes a string
def create_password_generator(string):

    # create an inner function that takes in a length
    # this function runs each time we call the outer function
    # The inner function has access to string from the outer function (this is due to LEGB) -- in this case its the enclosing scope
    def generate_password(length):
        # Access the string from outer function and apply length to it
        return "".join(random.choices(string, k=length))

    # return the inner function to the caller
    return generate_password


# Create var that's set to outer function and pass in a string
alpha_password = create_password_generator("abcdef")
# Call the var (that's set to the outer function) and pass in a number. This is how I pass in a val to the inner function
print(alpha_password(5))  # efeaa

# Inner function -- also called closure
# When invoke create_password_generator(string), it returns a function generate_password(length)
# The returned inner function KNOWS waht we did in the initial invocation (wiht the outer fucntion) BUT it
# also has functionality of its own -- so it needs to be defined as an inner funciton
# Put another way: it knows about and can access the stuff in teh outer funciton but it also has some of its OWN funciontality

# The inner funciton is defined when outer fucntion is executed -- so we create a new inner fucntion each time that the outerfunction is invoked
# IF the inner function is NOT used OR returned from within the outer funciton, then ite remains
# local to the outer function. It's common for the outer fucntion to return the inner one to its caller

# Each invocation of the outer function returns a separte version of generate_password
