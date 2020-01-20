d = {"a": 1, "b": 2, "c": 3, "d": 4}


def transform(funct1, funct2, d):
    update = {k: funct1(v) for k, v in d.items()}

    bool = {
        (k if funct2(v) == True else "odd"): (v if funct2(v) == True else v)
        for k, v in update.items()
    }

    return bool


print(transform(lambda x: x * x, lambda s: s % 2 == 0, d))


# { (some_key if condition else default_key):(something_if_true if condition
#           else something_if_false) for key, value in dict_.items() }
