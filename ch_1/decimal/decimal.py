number_1 = float(input("Enter a number: "))
number_2 = float(input("Enter a second number: "))


def add_floats(number_1, number_2):
    return f"{number_1 + number_2:.2f}"


print(add_floats(number_1, number_2))
