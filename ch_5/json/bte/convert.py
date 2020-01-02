import csv, json

csvfile = open("etc_passwd.csv", newline="", mode="r")
jsonfile = open("csv_to_json.json", newline="", mode="w")

all_rows = []
for row in csvfile:
    all_rows.append((row,))

for row in all_rows:
    json.dump(row, jsonfile)
    jsonfile.write("\n")
