
def anyjoin(sequence, glue=" "):
    
    new_string = ""

    for item in sequence:
        new_string += str(item) + glue
    return new_string

print(anyjoin('abc', '**'))