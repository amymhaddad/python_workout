import csv

# Option 1: read and write from csv files
with open("data.csv", "r") as reader, open("new_data.csv", "w") as writer:
    reader = csv.reader(reader, delimiter=" ")
    writer = csv.writer(writer, delimiter=" ")

    for rows in reader:
        each_row = []
        for row in rows:
            each_row.append(row.strip()[::-1])
        each_row.reverse()
        writer.writerow(each_row)

# Option 2: read and write from txt files
with open("data.txt", mode="r") as reader, open("new_data.txt", mode="w") as writer:
    for row in reader.readlines():
        writer.write(row.rstrip()[::-1] + "\n")
