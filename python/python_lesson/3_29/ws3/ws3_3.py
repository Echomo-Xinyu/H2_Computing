handler = open("iris.txt")
data = []
for line in handler:
    if line != None:
        # line = line.strip('\n')
        data.append(line.strip('\n').split(","))

print(data)