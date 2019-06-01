from flask import Flask, render_template, request
import sqlite3


def open_DB(db):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection


# def split_lines(lines):
#     return [ line.strip().split(",") for line in lines]

app = Flask("__name__")


@app.route("/")
def root():
    # file_handler = open("products.txt","r")
    # products_list=split_lines(file_handler.readlines()[1:])
    # file_handler.close()
    con = open_DB('catalogue.db')
    # cursor = con.execute("SELECT Name, Image FROM Products")
    cursor = con.execute("SELECT * FROM Products ORDER BY Price DESC")
    rows = cursor.fetchall()  # return a list of dictionary object
    con.close()
    return render_template("products.html", products=rows)


@app.route("/product")
def show_product_frm():
    return render_template("product_frm.html")

@app.route("/add", methods=["POST"])
def add_product():
    image_file_name = ""
    con = open_DB('catalogue.db')
    if "image" in request.files:
        image_file = request.files["image"]
        image_file_name = image_file.filename
        image_file.save("static/images/"+image_file_name)
    try:
        a, b, c, d = request.form['name'], request.form['description'], request.form['price'], image_file_name
        con.execute("INSERT INTO Products(Name, Description, Price, Image) VALUES(?, ?, ?, ?)", (a, b, c, d))
        con.commit()
    except:
        print("Database error")
    con.close()
    con = open_DB('catalogue.db')
    # cursor = con.execute("SELECT Name, Image FROM Products")
    cursor = con.execute("SELECT * FROM Products ORDER BY Price DESC")
    rows = cursor.fetchall()  # return a list of dictionary object
    con.close()
    return render_template("products.html", products=rows)
    # return render_template("products.html")


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
