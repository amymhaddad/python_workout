class HourTooLowError(Exception):
    pass


class HourTooHighError(Exception):
    pass


rates = {"Chico": 0.50, "Grancho": 0.70, "Harpo": 0.50, "Zeppo": 0.40}


def time_percentage(hour):
    if hour < 0:
        raise HourTooLowError(f"The hour is {hour}")

    elif hour >= 24:
        raise HourTooHighError(f"The hour is {hour}")

    return hour / 24


def calculate_tax(amount, province, hour):

    tax_amount = int(amount * (rates[province] * time_percentage(hour)))
    return f"${amount + tax_amount}"
