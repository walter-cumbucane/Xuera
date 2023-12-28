#!/usr/bin/python3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/ivanilson", methods=["post"])
def first():
    name = request.form.get("name")
    password = request.form.get("password")
    email = request.form.get("email")
    return render_template("success.html", name=name)


if __name__ == "__main__":
    app.run()
