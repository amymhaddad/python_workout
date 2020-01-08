def myxml(*args, **kargs):

    new_string = "<foo></foo>"
    index = new_string.find(">")

    if args:
        for arg in args:
            if arg != "foo":
                insert = new_string[: index + 1] + arg + new_string[index + 1 :]
                new_string = insert

    if kargs:

        k_v_pair = ""
        for k, v in kargs.items():

            k_v_pair += f"{k}='{v}' "

        insert = new_string[:index] + " " + k_v_pair.rstrip() + new_string[index:]
        new_string = insert

    return new_string
