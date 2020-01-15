
#Sum from user input, ignoring any non-numeric "words" that the string might contain.
user_input = "10 abc 20 de44 30 55fg 40"

sum_nums = sum(
    int(char)
    for char in user_input.split()
    if char.isdigit())  

# print(sum_nums)


