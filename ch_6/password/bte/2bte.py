# Write a function, doboth, that takes two functions as arguments (f1 and f2)
# and returns a single function, g.
# Invoking g(x) should return the same result as invoking f2(f1(x)).


def doboth(f1, f2):
    def g(x):
        return f1(x)

    return g
