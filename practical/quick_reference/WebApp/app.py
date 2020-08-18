from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask("__main__")

def open_db(db):
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    return con


@app.route("/")
def home():
    con = open_db("cookies.db")
    cur = con.execute("SELECT * FROM Flavour_info")
    flavour_info = {}
    for i in cur:
        flavour_info[i[0]] = i[1]
    con.close()
    return render_template("home.html",f_i = flavour_info)

@app.route("/submit",methods=["POST"])
def submit():
    con = open_db("cookies.db")
    name = request.form["name"]
    fla = request.form["flavour"]
    quan = request.form["quantity"]
    cur = con.execute("SELECT Customer_ID FROM Customers_info WHERE Customer_name=?",(name,))
    id_ = cur.fetchone()[0]
    con.execute("INSERT INTO Sales(Customer_ID,Flavour_name,Quantity) VALUES(?,?,?)",(id_,fla,quan))
    con.commit()
    con.close()
    return render_template("confirm.html",fla=fla,quan=quan)
    



app.run(debug=True)
