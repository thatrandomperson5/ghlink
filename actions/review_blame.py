import os
import sys
import requests
import tomli

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
for x in range(len(blame)):
    item = blame[x]
    if item.startswith(" "):
        blame[x] = {"type": "nochange", "content": item[1:]}
    elif item.startswith("+"):
        blame[x] = {"type": "add", "content": item[1:]}
    elif item.startswith("-"):
        blame[x] = {"type": "delete", "content": item[1:]}
print(blame)
for x in blame:
    if x["type"] != "nochange":
        # Standard checks
        toml = tomli.loads(x["content"])
        if toml.items()[0]["author"] != os.getenv("author"):
           raise ValueError(
               f"Wrong author edited a line: {toml.items()[0]['author']}, should be {os.getenv('author')}"
           )
