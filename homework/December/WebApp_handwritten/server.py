from flask import Flask, request, render_template, redirect
import sqlite3

# connect to database
def open_DB(db):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection

app = Flask(__name__)

@app.route("/")
def main():
    con = open_DB('catalogue.db')
    cur = con.execute("SELECT * FROM Namelist")
    rows = cur.fetchall()
    print(rows)
    con.close()
    return render_template("products.html", products=rows)

@app.route( "/add_item",methods=["GET"] )
def show_product_frm():
    return render_template("add_form.html")

@app.route("/add", methods=["POST"])
def add_location():
    image_file_name = ""
    if "image" in request.files:
        image_file = request.files["image"]
        image_file_name = image_file.filename
        pathway = "static/images/" + image_file_name
        # try:
        #     image_file.save(pathway)
        # except Exception as e:
        #     print(str(e))
        if image_file_name != "":
            image_file.save(pathway)
    try:
        con = open_DB("catalogue.db")
        con.execute(
            "INSERT INTO Namelist(Name, Address, Image) " +
            "VALUES(?, ?, ?)",
            (request.form["name"], request.form["address"],
             image_file_name))
        con.commit()
    except Exception as e:
        print(str(e))
    con.close()
    return redirect("/")

app.run(debug=True)