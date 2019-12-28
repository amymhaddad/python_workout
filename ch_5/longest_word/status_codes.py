from string import digits

counter = 0
for file in open("codes.txt"):
    each_line = file.split()

    for line in each_line:
        if line.startswith(("1", "2", "3", "4")) and len(line) == 3:
            counter += 1

print(counter)
