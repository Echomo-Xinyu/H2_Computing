import sqlite3

con = sqlite3.connect("catalogue.db")

try:
    con.execute("CREATE TABLE Locations " + 
                    " (Name TEXT PRIMARY KEY, Description TXT, Image TEXT )")
except Exception as err:
    print(str(err))

while True:
    name = input("Enter Location name: \n")
    if name == "":
        break
    description = input("Enter location description:\n")
    image = input("Enter image name:\n")
    try:
        con.execute("INSERT INTO Locations(Name, Description, Image) VALUES(?, ?, ?)", (name, description, image))
    except Exception as err:
        print(str(err), "Try another id")
        continue
    con.commit()
con.close()