def name_tri(name):
    triangle = []
    for index, letter in enumerate(name):
        if index == len(name) - 1:
            triangle.append(name)
            break
        elif index == 0:
            triangle.append(letter + "\n")
        else:
            triangle.append(name[: index + 1] + "\n")
    return "".join(triangle)


print(name_tri("Paul"))
