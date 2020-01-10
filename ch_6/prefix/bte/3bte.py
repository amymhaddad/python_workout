# Write a function, transform_lines, that takes three arguments:
# A function that takes a single argument, the name of an input file, and the name of an output file.
# Calling the function will run the function on each line of the input file, with the results written to the output file


def read(file):
    with open(file) as file_object:
        each_line = file_object.readlines()
        return each_line


def transform_lines(read, input_file, output_file):
    with open(output_file, mode="w") as writer:
        writer.writelines(read(input_file))


transform_lines(read, "input.txt", "output.txt")
