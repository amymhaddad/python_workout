with open("text.txt") as read_text, open("numbers.txt", "w") as write_numbers:

    numbers = []
    for words in read_text.readlines():
        for letter in words:
            if letter.isalpha():
                convert_letters = str(ord(letter))
                numbers.append(convert_letters)
            else:
                numbers.append(" ")
        numbers.append("\n")

    for number in numbers:
        write_numbers.write(number + " ")


with open("numbers.txt") as read_numbers, open("text.txt") as read_words:

    list_numbers = []
    for numbers in read_numbers:
        split_nums = numbers.strip().split(" ")
        for number in split_nums:
            try:
                convert_numbers = chr(int(number)).strip()
                list_numbers.append(convert_numbers)
            except ValueError:
                list_numbers.append(" ")
        list_numbers.append("\n")

    print("".join(list_numbers).strip())
