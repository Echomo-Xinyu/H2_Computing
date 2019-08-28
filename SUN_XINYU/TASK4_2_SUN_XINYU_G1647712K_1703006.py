import sqlite3

handle = open("MONITORS.txt", "r")
data = []
for line in handle:
	data.append(line.split(","))
handle.close()
# diction = ["SerialNumber", "Type", "Location", "DateOfPurchase", "WrittenOff", "DateCleaned"]
con = sqlite3.connect("equipment.db")
for i in range(len(data)):
	# for j in range(len(data[0])):
	con.execute("INSERT INTO Device(SerialNumber, Model, Location, DateOfPurchase, WrittenOff) VALUES (?, ?, ?, ?, ?)", (data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]))
	con.commit()
	con.execute("INSERT INTO Monitor(DateCleaned, SerialNumber) VALUES (?, ?)", (data[i][5], data[i][0]))
	con.commit()
con.close()

handle = open("LAPTOPS.txt", "r")
data = []
for line in handle:
	data.append(line.split(","))
handle.close()
# diction = ["SerialNumber", "Type", "Location", "DateOfPurchase", "WrittenOff", "WeightKg"]
con = sqlite3.connect("equipment.db")
for i in range(len(data)):
	# for j in range(len(data[0])):
	con.execute("INSERT INTO Device(SerialNumber, Model, Location, DateOfPurchase, WrittenOff) VALUES (?, ?, ?, ?, ?)", (data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]))
	con.commit()
	con.execute("INSERT INTO Labtop(WeightKg, SerialNumber) VALUES (?, ?)", (data[i][5], data[i][0]))
	con.commit()
con.close()

handle = open("PRINTERS.txt", "r")
data = []
for line in handle:
	data.append(line.split(","))
handle.close()
# diction = ["SerialNumber", "Type", "Location", "DateOfPurchase", "WrittenOff", "Toner", "DateChanged"]
con = sqlite3.connect("equipment.db")
for i in range(len(data)):
	con.execute("INSERT INTO Device(SerialNumber, Model, Location, DateOfPurchase, WrittenOff) VALUES (?, ?, ?, ?, ?)", (data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]))
	con.commit()
	con.execute("INSERT INTO Printer(Toner, DateChanged, SerialNumber) VALUES (?, ?, ?)", (data[i][5], data[i][6], data[i][0]))
	con.commit()
con.close()


