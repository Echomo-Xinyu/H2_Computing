from flask import Flask,render_template
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
    rows = cursor.fetchall() # return a list of dictionary object
    con.close()
    return render_template("products.html",products=rows)
    

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()

