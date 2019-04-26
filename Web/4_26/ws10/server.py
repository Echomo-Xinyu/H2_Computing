from flask import Flask
from flask import render_template
from flask import request
# from flask import *


app = Flask(__name__)


@app.route("/")  ## decorate function
def root():
    return render_template("product.html")


# @app.route("/submit", methods=["POST", "GET"])
# def submit():
#     w1 = float(request.form['weight1'])
#     m1 = float(request.form['mark1'])
#     w2 = float(request.form['weight2'])
#     m2 = float(request.form['mark2'])
#     score = m1 * (w1 / 100) + m2 * (w2 / 100)
#     # form, score are the jinja variables
#     return render_template("results.html", form=request.form, score=score)


app.run()
