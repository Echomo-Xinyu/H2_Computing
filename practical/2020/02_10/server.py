from flask import Flask,render_template,request

app = Flask(__name__)

H1_score = {
    "A":10,
    "B":8.75,
    "C":7.5,
    "D":6.25,
    "E":5,
    "S":2.5,
    "U":0
}

H2_score = {
    "A":20,
    "B":17.5,
    "C":15,
    "D":12.5,
    "E":10,
    "S":5,
    "U":0
}

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/calcualate", methods=["POST"])
def calcualate():
    score = H2_score[request.form["subj1"]] + H2_score[request.form["subj2"]] + H2_score[request.form["subj3"]] + H1_score[request.form["subj4"]] + H1_score[request.form["subj5"]] + H1_score[request.form["subj6"]]
    score_wmt = (H2_score[request.form["subj1"]] + H2_score[request.form["subj2"]] + H2_score[request.form["subj3"]] + H1_score[request.form["subj4"]] + H1_score[request.form["subj5"]] + H1_score[request.form["subj6"]] + H1_score[request.form["mt"]]) * 9 / 10.0
    actual_score = max(score, score_wmt)
    print(actual_score)
    return f"<h1>Your A level score is {actual_score}</h1>"

if __name__ == "__main__":
    app.run()