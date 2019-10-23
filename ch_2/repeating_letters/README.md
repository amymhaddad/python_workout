Write a function, most_repeating_word, that takes a sequence of strings as input. 

The function should return the string that contains the greatest number of repeated letters. 

That is, if words is set to

words = ['this', 'is', 'a', 'test', 'program']


then your function could return either program or test, since both contain a letter twice---r in the case of program, and t in the case of test. It doesn’t really matter which of these words is considered the "winner."

You will probably want to use Counter, from the collections module, which is perfect for counting the number of items in a sequence.