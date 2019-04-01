from random import randint
name = ""
for i in range(100):
    name = name + str(randint(0, 9))
    name = name + ".txt"
    try:
        fileHandle = open(name)
    except:
        continue
    data = fileHandle.read()
    print(data)
    fileHandle.close()