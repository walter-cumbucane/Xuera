#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/ivanilson")
def first():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
