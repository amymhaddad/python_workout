with open("etc.txt") as etc_reader, open("shell.txt", "w") as shell_writer:

    shell_name = {}
    for line in etc_reader.readlines():
        each_line = line.split(":")

        shell = each_line[-1].strip()

        shell_name.setdefault(shell, [])
        shell_name[shell].append(each_line[0])

    line_contents = ""
    for name, username in shell_name.items():
        # line_contents += name + ": "
        line_contents += f"{name}: "
        for user in username:
            line_contents += f"{user}, "
        line_contents += "\n"
    shell_writer.write(line_contents)
