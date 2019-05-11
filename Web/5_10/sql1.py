import sqlite3

con = sqlite3.connect("db1.db")

# con.execute("CREATE TABLE Book " +
#                 "(ID INTEGER PRIMARY KEY, Title TEXT)")

# id = input("Enter Book ID:\n")
# Title = input("Enter Book title:\n")
# con.execute("INSERT INTO Book(ID, Title) VALUES(?, ?)", (id, Title))

# id = input("Enter Book ID to delete:\n")
# con.execute("DELETE FROM Book WHERE ID is (?)", (id))
# con.execute("DELETE FROM Book WHERE ID = ?", (id,))

# cursor = con.execute("SELECT ID, Title FROM Book")
# for row in cursor:
#     print(row[0])

con.row_factory = sqlite3.Row
cursor = con.execute("SELECT ID, Title FROM Book")
for row in cursor:
    print(row["Title"])

# con.commit()
con.close()