# Write a function, getitem, that takes a single argument and return a function f.
# The returned f can then be invoked on any data structure whose elements can be selected via square brackets, and returns that item.
# So if I invoke f = getitem('a'), and if I have a dictionary d = {'a':1, 'b':2}, then f(d) will return 1.


def getitem(arg):
    def f(data_structure):
        return data_structure[arg]

    return f


d = {"a": 1, "b": 2}
f = getitem("a")
print(f(d))
