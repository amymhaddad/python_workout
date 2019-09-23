word_list = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz'] 

split_word_list = [group.split(" ") for group in word_list]

#Option 1: (missing the comma that separates each group of words)
# new_word_list = []
# group_list = []

# for words in split_word_list:
#     group_list.append(words[0])
#     group_list.append(words[1])
#     group_list.append(words[2])

# new_word_list.append(" ".join(group_list))
# print(new_word_list)

# Option 2
new_word_list = []

word_groups = ''

index = 0
while index < 3:
    for group in split_word_list:
        word_groups += group[index] + ' '
        
    new_word_list.append(word_groups)
    index += 1
    word_groups = ''
print(new_word_list)




# for i, word_group in enumerate(split_word_list):

# print(split_word_list)
# print(word_list)

# ['abc jkl stu', 'def mno vwx', 'ghi pqr yz']
