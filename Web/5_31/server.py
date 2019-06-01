from flask import Flask, render_template, request
import sqlite3

def open_DB(db):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection

app = Flask("__name__")

@app.route("/")
def root():
    con = open_DB("catalogue.db")
    cursor = con.execute("SELECT * FROM Locations")
    rows = cursor.fetchall()
    con.close()
    return render_template("main_menu.html", locations=rows)

@app.route("/addLocation", methods=["POST"])
def add_location():
    image_file_name = ""
    con = open_DB('catalogue.db')
    if "image" in request.files:
        image_file = request.files["image"]
        image_file_name = image_file.filename
        image_file.save("static/images/"+image_file_name)
    try:
        a, b, d = request.form['name'], request.form['description'], image_file_name
        con.execute("INSERT INTO Locations(Name, Description, Image) VALUES(?, ?, ?)", (a, b, d))
        con.commit()
    except:
        print("Database error")
    con.close()
    con = open_DB('catalogue.db')
    # cursor = con.execute("SELECT Name, Image FROM Products")
    cursor = con.execute("SELECT * FROM Locations")
    rows = cursor.fetchall()  # return a list of dictionary object
    con.close()
    return render_template("products.html", products=rows)
    # return render_template("products.html")

if __name__ == "__main__":
    app.run()