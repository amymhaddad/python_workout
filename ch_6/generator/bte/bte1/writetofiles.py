def copyfile(filename, *args):
    for arg in args:
        with open(filename) as myfile_reader, open(arg, "w") as writer_file:
            each_line = myfile_reader.readlines()

            for line in each_line:
                writer_file.write(line)


copyfile("myfile.txt", "copy1.txt", "copy2.txt")
