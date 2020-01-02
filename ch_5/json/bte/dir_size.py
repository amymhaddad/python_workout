import json, os, glob

dir_name = "scores"

all_files = glob.glob("../scores/*.json")


data = {}
for info in all_files:

    size = os.stat(info).st_size
    timestamp = round(os.stat(info).st_atime, 2)
    data[info] = [size, timestamp]


with open("size.json", "w") as json_data:
    json.dump(data, json_data)

with open("size.json", "r") as readin:
    data = json.load(readin)
