WORD_LIST = ["abc def ghi", "jkl mno pqr", "stu vwx yz"]

split_word_list = [group.split(" ") for group in WORD_LIST]


def create_new_word_list():
    """Create a new word list from WORD_LIST 
    that contains the groups of letters at each index for each string."""

    new_word_list = []
    word_groups = ""

    index = 0
    while index < 3:
        for group in split_word_list:
            word_groups += group[index] + " "

        new_word_list.append(word_groups)
        index += 1
        word_groups = ""
    return new_word_list


print(create_new_word_list())
