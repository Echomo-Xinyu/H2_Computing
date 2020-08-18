from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)

def openDB(db):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/submit", method="POST")
def submit():
    con = openDB("db.db")
    data = request.form["name"]
    con.execute("INSERT INTO Student(Name) VALUES(?)", (data, ))
    con.commit()
    return render_template("home.html")

app.run()


import socket
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("127.0.0.1", 1000))
while True:
    send = "\n"
    s1.sendall(send.encode())
    msg = s1.recv(1024).decode()
    print(msg)
s1.close()

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.bind(("127.0.0.1", 1000))

s2.listen()
s3, addr = s2.accept()
print("")
while True:
    msg = ""
    while "\n" not in msg:
        msg += s3.recv(1024).decode()
    print(msg)
s3.close()
s2.close()

from pymongo import MongoClient
client = MongoClient("localhost", 27017)
con = client["db"]["con"]
con.drop()

d = [{"1":1, "2":2}, {"1":1, "2":2}]
con.insert_many(d)
cur = con.find({"1":1}, {"_id":0, "2":1})
for i in cur:
    print(i)
