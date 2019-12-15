import re, operator

# Option 1
username_id = {}
with open("passwd.txt", "r") as f_object:
    lines = f_object.readlines()
    for i, line in enumerate(lines):
        if line.startswith("#") or line.startswith("\n"):
            continue
        parsed_line = line.strip("").split(":")[:3]
        user_name = re.sub(r"_", "", parsed_line[0])
        username_id[user_name] = parsed_line[-1]


for name, id in username_id.items():
    print(f"{name} {id}")

# Option 2
users = {}

with open("passwd.txt", mode="r") as f_object:
    lines = f_object.readlines()

    for line in lines:
        if not line.startswith(("\n", "#")):
            split_line = line.split(":")
            users[split_line[0]] = split_line[2]

for name, id in users.items():
    print(f"{name} {id}")
