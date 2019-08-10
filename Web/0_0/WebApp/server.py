from flask import Flask, render_template, request, redirect, url_for

import os
import sqlite3


# connect to database
def open_DB(db):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection


app = Flask("__name__")


@app.route("/")
def root():
    con = open_DB("catalogue.db")
    cur = con.execute("SELECT * FROM Locations")
    rows = cur.fetchall()
    # print(rows)
    con.close()
    return render_template("locations.html", locations=rows)


@app.route("/edit/<location>", methods=['GET'])
def edit_location(location):
    try:
        con = open_DB("catalogue.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM locations WHERE name=?", (location, ))
        row = cur.fetchone()
    except Exception as e:
        print(str(e))
    con.close()
    return render_template("location_edit.html", data=row)


@app.route( "/add_location",methods=["GET"] )
def show_product_frm():
    return render_template("location_add.html")

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
            image_file.save("?",(pathway,))
    try:
        con = open_DB("catalogue.db")
        con.execute(
            "INSERT INTO Locations(Name, Description, Image) " +
            "VALUES(?, ?, ?)",
            (request.form["name"], request.form["description"],
             image_file_name))
        con.commit()
    except Exception as e:
        print(str(e))
    con.close()
    return redirect("/")


@app.route("/update/<location>", methods=["POST"])
def update_location(location):
    image_file_name = ""
    if "image" in request.files:
        image_file = request.files["image"]
        image_file_name = image_file.filename
        pathway = "static/images/" + image_file_name
        # try:
        #     if image_file != "":
        #         image_file.save(pathway)
        # except:
        #     print("Hmm the bug is yet to handle")
        if image_file_name != "":
            image_file.save(pathway)
    try:
        con = open_DB("catalogue.db")
        cur = con.cursor()
        if request.form["submit"] == "update" and image_file_name == "":
            cur.execute(
                "UPDATE locations set name=?, description=? where name=?",
                (request.form["name"], request.form["description"], location))
        elif request.form["submit"] == "update" and image_file_name != "":
            cur.execute(
                "UPDATE locations set name=?, description=?, image=? where name=?",
                (request.form["name"], request.form["description"],
                 image_file_name, location))
        elif request.form["submit"] == "delete":
            cur.execute("DELETE FROM locations WHERE name=?", (location,))
            print("Product deleted")
        con.commit()
    except Exception as e:
        print("***" + str(e))
    con.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)