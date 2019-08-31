from flask import Flask, render_template, request, redirect
import sqlite3
app = Flask(__name__)
auth = False

def openDB():
    return sqlite3.connect("locations.db")

def deleteLink(q1, q2):
    con = openDB()
    if con.execute("SELECT COUNT(*) FROM Linking WHERE [From] = (?) AND [To] =  (?) ",(q1,q2)).fetchall()[0][0] != 0:
        con.execute("DELETE FROM Linking WHERE [From] = (?) AND [To] = (?)", (q1, q2))
        con.execute("DELETE FROM Linking WHERE [From] = (?) AND [To] = (?)", (q2, q1))
        con.commit()
        con.close()
        return True
    else:
        con.close()
        return False

def getLinks(query):
    con = openDB()
    cursor = con.execute("SELECT [To] FROM Linking WHERE [From] = (?)",(query,))
    links = cursor.fetchall()
    print(links)
    links = [str(i)[2:-3] for i in links]
    links.sort()
    return links

def reader(query=None):
    con = openDB()
    if query == None:
        cursor = con.execute("SELECT * FROM Locations")
        rows = cursor.fetchall()
    elif query == "-names":
        cursor=con.execute("SELECT Name FROM Locations")
        rows = cursor.fetchall()
    else:
        rows = []
        for i in query:
            cursor = con.execute("Select * FROM Locations where Name = ?", (i,))
            rows += cursor.fetchall()
        print(rows)
    con.close()
    return rows

def floor():
    con = openDB()
    cursor = con.execute("SELECT DISTINCT Floor FROM Locations")
    rows = [float(str(i)[1:-2]) for i in cursor.fetchall()]
    print(rows)
    con.close()
    return rows

def item(query):
    """returns one item only"""
    con = openDB()
    cursor = con.execute("SELECT * FROM Locations WHERE Name = (?)", (query,))
    item = cursor.fetchall()
    con.close()
    return item

@app.route("/floor/<floorNum>")
def redirFloor(floorNum):
    con = openDB()
    res = con.execute("SELECT * FROM Locations WHERE Floor = (?)",(floorNum,))
    res = res.fetchall()
    res.sort(key=lambda x:x[0])
    if auth:
        return render_template("adminMenu.html", floors=floor(), res=res)
    return render_template("menu.html", floors=floor(), res = res)

@app.route("/addLocation")
def addLocation():
    if auth:
        return render_template("addlocation.html", floors=floor(), userScrewedUp = False)
    else:
        return "only if u log in"

@app.route("/link", methods=["POST"])
def addLink():
    con = openDB()
    loc1 = request.form["location1"].lower()
    loc2 = request.form["location2"].lower()
    #check if both locations exist
    if con.execute("SELECT COUNT(*) FROM Locations WHERE Name = ?",(loc1,)).fetchall()[0][0] != 0 and con.execute("SELECT COUNT(*) FROM Locations WHERE Name = ?",(loc2,)).fetchall()[0][0] != 0 and loc1 != loc2 and con.execute("SELECT COUNT(*) FROM Linking WHERE [To] = ? and [From] = ?",(loc1, loc2)).fetchall()[0][0] == 0:
        con.execute("INSERT INTO Linking([From],[To]) VALUES (?, ?)", (loc1, loc2))
        con.execute("INSERT INTO Linking([From],[To]) VALUES (?, ?)", (loc2, loc1))
        con.commit()
    else:
        #print(con.execute("SELECT COUNT(*) FROM Locations WHERE Name = ?",(loc1,)).fetchall()[0][0], con.execute("SELECT COUNT(*) FROM Locations WHERE Name = ?",(loc2,)).fetchall()[0][0])
        con.close()
        names = [str(i)[2:-3] for i in reader("-names")]
        return render_template("addlink.html", floors=floor(), locationNames = names, userScrewedUp = True)

    con.close()   
    return redirect("/admin")

@app.route("/addLink")
def redirAddLink():
    if auth:
        names = [str(i)[2:-3] for i in reader("-names")]
        return render_template("addlink.html", floors=floor(), locationNames = names)
    else:
        return "only if u log in"

@app.route("/add", methods=["POST"])
def addItem():
    print("running")
    image_file_name = ""
    if "image" in request.files and request.files["image"].filename != "":
        print("running1")
        image_file = request.files["image"]
        image_file_name = image_file.filename
        image_file.save("static/images/" + image_file_name) 
    else:
    	return "no image no add >:("
    try:
        print("running2")
        con = sqlite3.connect("locations.db")
        con.execute("INSERT INTO Locations(Name,Description,Image,Floor) VALUES (?,?,?,?)", (request.form['name'],request.form['desc'],image_file_name, request.form['floor']))
        con.commit()
        con.close()
        
    except Exception as e:
        return str(e)
    return redirect("/admin")

@app.route("/search", methods=["POST"])
def search():
    query = request.form["query"].lower()
    con = openDB()
    res = con.execute("SELECT * FROM Locations WHERE Name LIKE ?", ('%{}%'.format(query),)).fetchall()
    if auth:
        return render_template("adminMenu.html", res = res, floors=floor())
    return render_template("menu.html", res=res, floor=floor())


@app.route("/admin")
def redirAdmin():
    if auth:
        res = reader()
        floors = floor()
        res.sort(key=lambda x:x[0])
        return render_template("adminMenu.html",floors= floor(), res=res)
    else:
        return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    if request.form["username"] == "superadmin" and request.form["password"] == "p4ssw0rd":
        global auth
        auth = True
        return redirect("/admin")
    else:
        return redirect("/loginpage")

@app.route("/loginpage")
def redirLogin():
    return render_template("login.html", floors=floor())


@app.route("/")
def root():
    global auth
    auth = False
    res = reader()
    res.sort(key=lambda x:x[0])
    floors = floor()
    return render_template("menu.html",res=res, floors=floors)

@app.route("/item/<itemName>")
def displayItem(itemName):
    return render_template("item.html", floors = floor(), i = item(itemName), links=reader(getLinks(itemName)), auth=auth)

@app.route("/edit/<itemName>")
def redirEdit(itemName):
    return render_template("edit.html", floors=floor(), i = item(itemName))

@app.route("/itemEdit/<itemName>", methods=["POST"])
def editItem(itemName):
    con = openDB()
    data = request.form
    #return str(os.stat(request.files["image"]))
    image_file_name = item(itemName)[0][2]
    if "image" in request.files and request.files["image"].filename != "":
        image_file = request.files["image"]
        #return str(type(image_file==None))
        image_file.save("static/images/" + image_file_name)

    try:
        con.execute("UPDATE Locations SET Name = ?, Description = ?, Floor = ? WHERE Name = ?",(data["name"],data["desc"],data["floor"], itemName))
        con.commit()
    except Exception as err:
        #return str(err)
        pass
    con.close()
    return redirect("/admin")

@app.route("/delete/<location>")
def deleteLocation(location):
    con = openDB()
    if con.execute("SELECT COUNT(*) FROM Locations WHERE Name = ?",(location,)).fetchall()[0][0] != 0:
        con.execute("DELETE FROM Locations Where Name = ?",(location,))
        con.execute("DELETE FROM Linking Where [From] = ?",(location,))
        con.execute("DELETE FROM Linking Where [To] = ?",(location,))
        con.commit()
    con.close()
    return redirect("/admin")
    

@app.route("/linkDelete/<q1>/<q2>")
def linkDelete(q1,q2):
    deleteLink(q1,q2)
    return redirect("/item/" + q1)


app.run(debug=True)

