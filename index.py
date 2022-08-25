from flask import Flask, redirect, abort
import tomli

app = Flask(__name__)

with open("public/refs.toml", "rb") as f:
    data = tomli.load(f)


@app.route("/")
def home():
    return "hello world"


@app.route("/hub/<key>")
def github(key):
    if key not in data["github"].keys():
        abort(404)
    return redirect(data["github"][key]["val"])
