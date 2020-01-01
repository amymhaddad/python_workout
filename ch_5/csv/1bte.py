import csv

user_numbers = input("Enter a list of numbers separated by a space: ")
user_delimiter = input("Enter a delimiter: ")


list_of_numbers = [int(number) for number in user_numbers if number.isdigit()]

with open("passwd.txt", mode="r") as passwd, open(
    "csv_etc_passwd.csv", mode="w"
) as output:
    reader = csv.reader(passwd, delimiter=":")
    writer = csv.writer(output, delimiter="\t")

    for line in reader:
        if line[0].startswith("#"):
            continue
        else:
            for num in list_of_numbers:
                try:
                    writer.writerow((line[num]))
                except KeyError:
                    break
