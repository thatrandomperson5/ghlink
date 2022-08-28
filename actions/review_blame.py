import os
import sys
import requests


def getitems(l):
    l = l.split(" ")
    for x in l:
        l[l.index(x)] = eval(x)
    return l


diff = getitems(os.getenv("DIFF"))
print(diff)
if diff != ["public/refs.toml"]:
    sys.exit("You can only edit public/refs.toml")
with open("public/refs.diff", "r") as f:
    blame = f.readlines()
blame = blame[4:]
author = os.getenv("author")
print(author)
print(blame)
# fmt: off
# if z["author"] != os.getenv("author"):
#    raise ValueError(
#        f"Wrong author: {z['author']}, should be {os.getenv('author')}"
#    )
# fmt: on
