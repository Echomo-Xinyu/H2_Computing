CREATE TABLE Device (
	SerialNumber TEXT PRIMARY KEY,
	Model TEXT,
	Location TEXT,
	DateOfPurchase TEXT,
	WrittenOff BOOL
);

CREATE TABLE Monitor (
	DateCleaned TEXT,
	SerialNumber TEXT,
	FOREIGN KEY (SerialNumber) REFERENCES Device(SerialNumber)
);

CREATE TABLE Labtop (
	WeightKg INT,
	SerialNumber TEXT,
	-- PRIMARY KEY (SerialNumber),
	FOREIGN KEY (SerialNumber) REFERENCES Device(SerialNumber)
);

CREATE TABLE Printer (
	Toner TEXT,
	DateChanged TEXT,
	SerialNumber TEXT,
	FOREIGN KEY (SerialNumber) REFERENCES Device(SerialNumber)
)
