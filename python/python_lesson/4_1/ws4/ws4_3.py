
while True:
    x = input("Please input an integer number. A string will be the end of the program.")
    fileHandle = open("RATIONALS.TXT", "a")
    try:
        x = int(x)
    except ValueError:
        break
    except:
        print("This is not a rational number.")
    fileHandle.write(str(x)+"\n")
    fileHandle.close()