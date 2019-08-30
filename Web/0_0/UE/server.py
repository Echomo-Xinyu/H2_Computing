from flask import Flask, render_template, request, redirect
import sqlite3

# admin mode
authen = False

def open_db(db="locations.db"):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection

app = Flask("__name__")

@app.route("/")
def root():
    global authen
    authen = False
    return render_template("main.html")

@app.route("/login_option", methods=["GET", "POST"])
def login_option():
    if request.form["submit"] == "admin":
        return render_template("login.html")
    else:
        return render_template("menu.html")

def _hash(string):
    result = ""
    for i in range(len(string)):
        result += str((i + 1) * ord(string[i]))
    return result

@app.route("/login", methods=["POST"])
def login():
    input_name, input_password = request.form["username"], request.form["password"]
    con = open_db("locations.db")
    try:
        cur = con.execute("SELECT * FROM Users WHERE Name=?", input_name)
        row = cur.fetchone()
        print("1")
        if _hash(input_password) == row["PasswordHashed"]:
            return redirect("/admin")
        else:
            # return redirect("/login_option")
            return render_template("main.html")
    except:
        # return redirect("/login_option")
        return render_template("main.html")

@app.route("/admin")
def admin():
    con = open_db("locations.db")
    cur = con.execute("SELECT * FROM Locations")
    rows = cur.fetchall()
    # print(rows)
    con.close()
    return render_template("admin.html", locations=rows)

@app.route("/add_location", methods=["GET"])
def add_location():
    return render_template("add_location.html")

@app.route("/add", methods=["POST"])
def add():
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
        con = open_db("catalogue.db")
        con.execute(
            "INSERT INTO Locations(Name, Description, Image) " +
            "VALUES(?, ?, ?)",
            (request.form["name"], request.form["description"],
             image_file_name))
        con.commit()
    except Exception as e:
        print(str(e))
    con.close()
    return redirect("/admin")

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
        con = open_db("catalogue.db")
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
    return redirect("/admin")

@app.route("/visitor")
def visitor():
    con = open_db("locations.db")
    cursor = con.execute("SELECT * FROM Locations")
    rows = cursor.fetchall()
    con.close()
    rows.sort(key = lambda x:x[0])
    return render_template("menu.html", rows = rows)

@app.route("/item/<location>")
def displayItem(location):
    con = open_db("locations.db")
    cursor = con.execute("SELECT * FROM Locations WHERE Name = (?)", (location, ))
    stuff = cursor.fetchone()
    cursor = con.execute("SELECT [To] FROM Linking WHERE [From] = (?)", (location, ))
    links = cursor.fetchall()
    links = [str(i)[2:-3] for i in links]
    links.sort()
    lis_links = []
    for i in links:
        cursor = con.execute("SELECT * FROM Locations WHERE Name = (?)", (i, ))
        lis_links += cursor
    con.close()
    return render_template("item.html", i=stuff, links=lis_links, auth=authen)

@app.route("/edit/<location>")
def dirEdit(location):
    con = open_db("locations.db")
    cursor = con.execute("SELECT * FROM Locations WHERE Name = (?)", (location, ))
    item = cursor.fetchone()
    con.close()
    return render_template("edit.html", i=item)

@app.route("/editLocation_/<location>", methods=["POST"])
def editItem(location):
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
        con = open_db("locations.db")
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
    return redirect("/admin")

@app.route("/delete/<location>")
def deleteLocation(location):
    con = open_db("locations.db")
    if con.execute("SELECT COUNT(*) FROM Locations WHERE Name = ?", (location, )).fetchone()[0][0] != 0:
        con.execute("DELETE FROM Locations WHERE Name = (?)", (location, ))
        con.execute("DELETE FROM Linking WHERE [From] = (?)", (location, ))
        con.execute("DELETE FROM Linking WHERE [To] = ?", (location, ))
        con.commit()
    con.close()
    return redirect("/admin")

@app.route("/deleteLink/<l1>/<l2>")
def deleteLink(l1, l2):
    con = open_db("locations.db")
    if con.execute("SELECT COUNT(*) FROM Linking WHERE [From] = (?) AND [To] = (?)", (l1, l2)).fetchall()[0][0] != 0:
        con.execute("DELETE FROM Linking WHERE [From] - (?) AND [To] = (?)", (l1, l2))
        con.execute("DELETE FROM Linking WHERE [From] = (?) AND [To] = (?)", (l1, l2))
        con.commit()
        con.close()
        return True
    else:
        con.close()
        return False

print(_hash("Password1"))
app.run(debug=True)