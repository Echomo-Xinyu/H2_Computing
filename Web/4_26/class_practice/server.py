from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("data_frm.html")

@app.route("/calculate", methods=["POST"])
def calulate():
    w = float(request.form["w"])
    h = float(request.form["h"])
    bmi_score = w / (h * h)
    return render_template("results.html", height=h, weight=w, bmi=bmi_score)

app.run()