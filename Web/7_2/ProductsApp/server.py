from flask import Flask,render_template,request,redirect, url_for

import os
def split_lines(lines):
    return list(map(lambda x: x.split(","),lines))

## DB boiler plates **
import sqlite3
def open_DB(db):
    connection=sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection

app = Flask("__name__")

@app.route("/")
def root():
    #file_handler = open("products.txt","r")
    #products_list=split_lines(file_handler.readlines()[1:])
    con = open_DB('catalogue.db')
    cur=con.execute("SELECT * FROM Products")
    rows=cur.fetchall()
    print(rows)
    con.close()
    #file_handler.close()

    return render_template("products.html",products=rows)

@app.route("/edit/<product>", methods=['GET'])
def edit_product(product):
    try:
        con = open_DB('catalogue.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM products where name=?", (product,))
        row = cur.fetchone()
    except Exception as e:
        print(str(e))
    con.close()
    return render_template("product_edit.html", data=row)
    

@app.route( "/product",methods=["GET"] )
def show_product_frm():
    return render_template("product_frm.html")

@app.route("/add", methods=["POST"])
def add_product():
    image_file_name=""
    
    if "image" in request.files:
        image_file = request.files["image"]
        image_file_name=image_file.filename
        image_file.save("static/images/"+ image_file_name)
    try:
        con=open_DB("catalogue.db")
        con.execute("INSERT INTO Products(Name, Description, Price,Image) " +
                    "VALUES(?,?,?,?)",
                    (request.form["name"], request.form["description"],request.form["price"],image_file_name))
        con.commit()
    except Exception as err:
        print(str(err))
    con.close()
    return redirect("/")

@app.route("/update/<product>", methods=['POST'])
def update_product(product):
    image_file_name = ""
    if "image" in request.files:
        image_file = request.files["image"]
        image_file_name = image_file.filename
        if image_file_name != "":
            image_file.save("static/images/" + image_file_name)
    try:
        con = open_DB("catalogue.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        if request.form["submit"] == "update" and image_file_name == "":
            cur.execute("UPDATE products set name=?, description=?, price=? where name=?",
                        (request.form["name"], request.form["description"], request.form["price"], product))
        elif request.form["submit"] == "update" and image_file_name != "":
            cur.execute("UPDATE products set name=?, description=?, price=?, image=? where name=?",
                        (request.form["name"], request.form["description"], request.form["price"], image_file_name, product))
        elif request.form["submit"] == "delete":
            cur.execute("DELETE FROM products WHERE name=?", (product,))
            msg = "Product deleted"
        con.commit()
        con.close()
    except Exception as e:
        print("***" + str(e))
        con.close()
    return redirect("/")

if __name__ == "__main__":
    app.run()

