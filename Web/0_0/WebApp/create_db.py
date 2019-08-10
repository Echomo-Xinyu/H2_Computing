import sqlite3

con = sqlite3.connect("catalogue.db")
try:
    con.execute("CREATE TABLE Locations " +
                "(Name TEXT PRIMARY KEY, Description TEXT, Image TEXT)")
except Exception as e:
    print(str(e))

while True:
    name = input("Enter Location Name:\n")
    if name == "":
        break
    description = input("Enter location Description:\n")
    image = input("Enter image name:\n")
    try:
        con.execute(
            "INSERT INTO Locations(Name, Description, Image) VALUES(?, ?, ?)",
            (name, description, image))
    except Exception as e:
        print(str(e))
        print("Try again")
        continue
    con.commit()
con.close()