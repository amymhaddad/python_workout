# From /etc/passwd, create a dict in which the keys are the usernames (as in the main exercise),
# and the values are themselves dicts with keys (and appropriate values) for user ID, home directory, and shell.

import re

users = {}

with open("passwd.txt") as file_object:
    rows = file_object.readlines()

    for row in rows:
        if row.startswith(("#", "\n")):
            continue
        else:
            total_rows = row.split(":")
            username = re.sub(r"_", "", total_rows[0])
            users[username] = {
                "userID": total_rows[2],
                "Home Directory": total_rows[-2],
                "Shell": total_rows[-1].strip("\n"),
            }
