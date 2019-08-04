import sqlite3
con = sqlite3.connect("catalogue.db")
try:
    con.execute("CREATE TABLE Products " +
                   "(Name TEXT PRIMARY KEY, Description TEXT, Price REAL, Image TEXT )")
except Exception as err:
    print(str(err))
while True:
    name = input("Enter Product name:")
    if name == "":
        break
    description=input("Enter Product Description:")
    price=input("Enter Price:")
    image=input("Enter image name:")
    try:
        con.execute("INSERT INTO Products(Name,Description,Price,Image) VALUES(?,?,?,?)",
                     (name,description,price,image))
    except Exception as err:
        print(str(err), "Try another id")
        continue
    con.commit()
con.close()