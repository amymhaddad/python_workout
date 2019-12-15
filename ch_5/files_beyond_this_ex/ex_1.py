# ex: 1
# Read through /etc/passwd, creating a dict in which user login shells (the final field on each line) are the keys.
# Each value will be a list of the users for whom that shell is defined as their login shell.

import re


def read_file(file):
    with open(file) as f_object:
        rows = f_object.readlines()
    return rows


def shells_with_usernames(rows):

    users = {}
    total_usernames = ""
    user_login_shell = ""
    for lines in rows:
        each_row = lines.split(":")
        if each_row[0].startswith(("#", "\n")):
            continue
        else:
            username = re.sub(r"\_", "", each_row[0])
            shell = re.sub(r"\s+", "", each_row[-1])

            if not user_login_shell:
                user_login_shell = shell

            if shell == user_login_shell:
                total_usernames += username + " "

            elif shell != user_login_shell:

                user_login_shell = shell
                total_usernames = username

        users[user_login_shell] = [total_usernames]
    return users


print(shells_with_usernames(read_file("passwd.txt")))
