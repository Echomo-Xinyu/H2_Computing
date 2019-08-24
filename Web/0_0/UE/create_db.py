import sqlite3

db = sqlite3.connect("locations.db")
db.execute("CREATE TABLE IF NOT EXISTS Locations (Name TEXT PRIMARY KEY, Description TEXT, Image TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS Linking ('From' TEXT, 'To' TEXT)")
db.execute("CREATE TABLE IF NOT EXISTS Users (Name TEXT PRIMARY KEY, PasswordHashed TEXT)")
db.commit()
db.close()