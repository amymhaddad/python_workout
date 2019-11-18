def dictdiff(d1, d2):
    new_dict = {}

    unique_keys = set(d1.keys()) | set(d2.keys())

    for k in unique_keys:
        d1_value = [d1.get(k)]
        d2_value = [d2.get(k)]

        if d1_value != d2_value:
            new_dict[k] = new_dict.get(k, d1_value + d2_value)

    return new_dict
