# Using an "etc/password" file, what different shells (i.e., command interpreters, named in the final field on each line) are assigned to users? Use a set comprehension to gather them.

unique_shells = {
    lines.split(":")[-1].strip() for lines in open("pssword_etc.txt").readlines()
}
