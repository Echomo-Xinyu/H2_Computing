from flask import Flask
from flask import render_template
from flask import request
# from flask import *


app = Flask(__name__)


@app.route("/")  ## decorate function
def root():
    return render_template("form1.html")


@app.route("/submit", methods=["POST", "GET"])
def submit():
    output = "Hello World"
    return output


app.run()
