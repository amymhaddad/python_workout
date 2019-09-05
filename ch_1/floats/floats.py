number = "1234.5678"


def new_number(number, before, after):
    before_decimal = ""
    after_decimal = ""
    decimal = number.find(".")

    for i, num in enumerate(str(number)):
        if i < decimal:
            before_decimal += number[i]
        elif i > decimal:
            after_decimal += number[i]

    return before_decimal[before:] + "." + after_decimal[:after]


print(new_number(number, 2, 3))
