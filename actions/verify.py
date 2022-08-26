import tomli
import os
import sys
from urllib.parse import urlparse

with open("public/refs.toml", "rb") as f:
    toml = tomli.load(f)
authorcount = {}
for w, x in toml.items():
    if type(x) != dict:
        raise SyntaxError(f"Toml Data invalid: {x}")
    for y, z in x.items():
        if type(x) != dict:
            raise SyntaxError(f"Toml Data invalid: {x}")
        if type(z["val"]) != str:
            raise TypeError("Values can only be strings.")
        if type(z["author"]) != str:
            raise TypeError("Values can only be strings.")
        # if z["author"] != os.getenv("author"):
        # raise ValueError(f"Wrong author: {z['author']}, should be {os.getenv('author')}")
        url = urlparse(z["val"])
        if not url.hostname.split(".")[-2:] in [["github", "com"], ["github", "io"]]:
            raise ValueError("URL is not a valid github url.")
        if authorcount.get(z["author"]):
            authorcount[z["author"]] += 1
        else:
            authorcount[z["author"]] = 1
        if authorcount[z["author"]] > 5:
            sys.exit("To many url's by author.")
