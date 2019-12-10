def convert_hex(user_number):
    hex_value = 0
    for i, number in enumerate(reversed(user_number)):
        hex_value += int(number, 16) * (16 ** i)
    return hex_value
