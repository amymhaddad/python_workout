Exercise 1:
The dict.update method merges two dicts. Write a function that takes any number of dicts, and returns a dictionary that reflects the combination of all of them. If the same key appears in more than one dictionary, then the most recently merged dict’s value should appear in the output.

Exercise 2:
Write a function that takes any even number of arguments and returns a dict based on them. The even-indexed arguments become the dict keys, while the odd-numbered arguments become the dict values. Thus, calling the function with the arguments ('a', 1, 'b', 2) will result in the dict {'a':1, 'b':2} being returned.

Exercise 3:
Write a function, dict_partition, that takes one dictionary (d) and a function (f) as arguments. dict_partition will return two dictionaries,each containing key-value pairs from d. The decision regarding where to put each of the key-value pairs will be made according to the output from f, which will be run on each key-value pair in d. If f returns True, then the key-value pair will be put in the first output dict. If f returns False, then the key-value pair will be put in the second output dict.