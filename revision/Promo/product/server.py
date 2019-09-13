from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/login", methods=["POST"])
def login():
    TextA, TextB = request.form["TextA"], request.form["TextB"]
    print(TextA, TextB)
    return render_template("main.html")

app.run()
