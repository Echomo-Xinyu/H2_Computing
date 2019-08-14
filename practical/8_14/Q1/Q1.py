data = {}
record = []
client = []
    

handle = open("WEBLOG.txt")
for line in handle:
    for i in line:
        if i == "|":
            index = line.index(i)
            break
    current_client = line[:index]
    current_datetime = line[index+1:]
    #     print(client)
    #     print(datetime)
    data[current_datetime] = current_client
handle.close()
for key, value in data.items():
#     print(key)
#     print(value)
    if value not in client:
        record.append([value, key])
        client.append(value)
    else:
        record[client.index(value)] = record[client.index(value)] + [key]

for i in range(len(record)):
    print(record[i][0])


handle = open("SUMMARY.txt", "w")
# for key, value in data.items():
for i in range(len(record)):
    string = ""
    string += "{0:15}".format(record[i][0])
    for j in range(1,len(record[i])):
        string+=record[i][j]
    handle.write(string)
handle.close()