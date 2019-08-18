# this is to create 3NF databases for worksheet T3W5
# and it turns out no need for that, simply draw the diagram with pen
import sqlite3

def open_DB(db):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection


