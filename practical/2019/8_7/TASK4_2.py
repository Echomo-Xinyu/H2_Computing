import sqlite3

connection = sqlite3.connect("Portal.db")

handle = open("USERS.TXT", "r")


def d2k(d, k):
    result = ""
    mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while d > 0:
        digit = mapping[d % k]
        result = digit + result
        d = d // k
    return result


def hash_f(str):
    result = 0
    for i in range(len(str)):
        result += ord(str[i])
    return d2k(result, 16)


# data = []
i = 0
for line in handle:
    if i == 0:
        i += 1
        continue
    line = line.split(",")
    name = line[0]
    login_id = line[2]
    password_hash = hash_f("19SH07njc")
    connection.execute(
        "INSERT INTO User(Name, LoginID, PasswordHash) VALUES(?, ?, ?);",
        (name, login_id, password_hash))
    connection.commit()

connection.close()
