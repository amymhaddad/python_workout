# Use a dict comprehension to create a dictionary in which the keys are usernames and
# the values are (integer) user IDs, based on a Unix-style /etc/passwd file.

usernames_ids = {
    lines.split(":")[0]: lines.split(":")[2] for lines in open("text.txt").readlines()
}


print(usernames_ids)
