This file contains three exercises:


Exercise 1:
Write a function, mysum_bigger_than, that takes a first argument, preceding \*args. That argument indicates the threshold for including an argument in the sum. Thus, calling mysum_bigger_than(10, 5, 20, 30, 6) would return 50 — because 5 and 6 aren’t greater than 10. This function should similarly work with any types, and assumes that all of the arguments are of the same type. Note that > and < work on many different types in Python, not just on numbers; with strings, lists, and tuples, it refers to their sort order.


Exercise 2:
Write a function, sum_numeric, which takes any number of arguments. If the argument is or can be turned into an integer, then it should be added to the total. Those arguments which cannot be handled as integers should be ignored. The result is the sum of the numbers. Thus, sum_numeric(10, 20, 'a', '30', 'bcd') would return 60. Notice that even if the string 30 is an element in the list, it’s converted into an integer and added to the total.


Exercise 3:
Write a function that takes a list of dictionaries, and returns a single dictionary that combines all of the keys and values. If a key appears in more than one argument, then the value should be a list containing all of the values from the arguments.