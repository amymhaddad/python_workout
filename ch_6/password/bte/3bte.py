# Write a function, withfiles, that takes a glob-style pattern of filenames.
# It should return a function f that takes a single argument g, another function.
# When we invoke f, it iterates over each of the filenames returned by glob, opening each file and passing it to g.
# The output from f is a dictionary in which the filenames are the keys and the values are the results of g being invoked on each file.

import glob

filenames = []
for name in glob.glob("./files_2bte/*.txt"):
    filenames.append(name)


dict = {}


def withfiles(filenames):
    def f(g):
        for file in filenames:
            dict.setdefault(file, [])

            with open(file) as file_obj:
                content = file_obj.readlines()
                for lines in content:
                    return g(lines)

    return f


def g(lines):
    for name, values in dict.items():
        values.append(lines)
    return dict


file = withfiles(filenames)
print(file(g))
