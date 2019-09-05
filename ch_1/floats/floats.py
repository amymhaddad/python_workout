number = 1234.5678


def new_number(number, before, after):
    str_number = str(number)
    before_decimal = ""
    after_decimal = ""
    decimal = str_number.find(".")

    for i, num in enumerate(str_number):
        if i < decimal:
            before_decimal += str_number[i]
        elif i > decimal:
            after_decimal += str_number[i]

    return before_decimal[before:] + "." + after_decimal[:after]


print(new_number(number, 2, 3))
