
Write a Python program that asks the user to enter to enter an English word. Your program should then print the word, translated into Pig Latin. You may assume the the word contains no capital letters or punctuation

If the word begins with a vowel (a, e, i, o, or u), then add way to the end of the word. So air becomes airway and eat becomes eatway.
If the word begins with any other letter, then we take the first letter, put it on the end of the word, and then add ay. Thus, python becomes ythonpay and computer becomes omputercay.

Handle capitalized words: If a word is capitalized (i.e., the first letter is capitalized, but the rest of the word isn’t), then the Pig Latin translation should be similarly capitalized.

Handle punctuation: If a word ends with punctuation, then that should be shifted to the end of the translated word.
Consider an alternative version of Pig Latin, in which we don’t check to see if the first letter is a vowel, but rather we check to see if the word contains two different vowels. Thus, "wine" would have "way" added to the end, but "wind" would be translated into "indway". How would you check for two different vowels in the word?