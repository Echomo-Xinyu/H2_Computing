from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask("__name__")

@app.route("/")
def root():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    connection = sqlite3.connect("portal.db")
    cursor = connection.execute("SELECT * FROM User")
    for row in cursor:
        print(row[0]. row[1])
    return True

app.run(debug=True)