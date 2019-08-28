from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask("__name__")

@app.route("/")
def root():
	return render_template("main.html")

app.run()