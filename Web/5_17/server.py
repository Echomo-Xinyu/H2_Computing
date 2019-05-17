# this file is just to record down the class notes without practical purpose
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    con = sqlite3.connect("catalogue.db")
    # convert a cursor to a dictionary object. without the statement it will give a tuple
    con.row_factory = sqlite3.Row
    # database cursor, similar to iterator in python
    # replace DESC with ASC to get ascending order
    cursor = con.execute("SELECT * FROM products ORDER BY price DESC")
    # rows: a list of dictionary objects
    rows = cursor.fetchall()
    # # the following block is for tuple condition
    # # r is a tuple
    # for r in cursor:
    #     print(r[0], r[1], r[2])
    for r in rows:
        print(r["name"])

    return render_template("someweb.html", rows=rows)