import os


def getitems(l):
    l = l.split(" ")
    for x in l:
        l[l.index(x)] = eval(x)
    return l


diff = getitems(os.getenv("DIFF"))
print(diff)
if diff != ["public/refs.toml"]:
    sys.exit("You can only edit public/refs.toml")
