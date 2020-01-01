import csv

# Option 1
# details = []
# for lines in open("passwd.txt"):
#     if lines.startswith("#"):
#         continue
#     else:
#         each_line = lines.split(":")
#         user_info = [each_line[0], each_line[2]]
#         details.append(user_info)


# with open("csv_etc_passwd.csv", "w", newline='\n') as csv_obj:
#     user_details = csv.writer(csv_obj, delimiter="\t")
#     for person in details:
#         user_details.writerow(person)


# Option 2
# with open("passwd.txt", mode="r") as csvfile, open("csv_etc_passwd.csv", "w", newline='\n') as csvobj:
#     file_reader = csv.reader(csvfile, delimiter=":")
#     user_details = csv.writer(csvobj, delimiter="\t")

#     details = []
#     for row in file_reader:
#         if row[0].startswith("#"):
#             continue
#         else:
#             user_info = [row[0], row[2]]
#             details.append(user_info)

#     for person in details:
#         user_details.writerow(person)


# Option 3
import csv

with open("passwd.txt", mode="r") as passwd, open("csv_etc_passwd.csv", "w") as output:
    read = csv.reader(passwd, delimiter=":")
    write = csv.writer(output, delimiter="\t")

    for record in read:
        if len(record) > 1:
            write.writerow((record[0], record[2]))
