import sqlite3

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



connection = sqlite3.connect("Portal.db")
connection.row_factory = sqlite3.Row
while True:
    login_id = input("Please type your login id:\n")
    password = input("Please input your password:\n")
    try:
        print("start trying")
        cursor = connection.execute("SELECT * FROM User WHERE Name is (?)", ("Jolee Driuzzi",))
        
        for i in cursor:
            row = i
        # print(row)
        existing_login_id, pw_h = row["LoginID"], row["PasswordHash"]
        # print(existing_login_id, pw_h)
        if login_id == existing_login_id.strip() and pw_h.strip() == hash_f(password):
            print("Successful Login")
            break
    except Exception as e:
        print(str(e))
        print("Please re-enter the login id and password")
    # break
