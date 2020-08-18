CREATE TABLE "Student" (
	"MatricNo"	TEXT,
	"Name"	TEXT NOT NULL,
	"Class"	TEXT NOT NULL,
	"IndexNo"	INTEGER NOT NULL,
	"Gender"	TEXT NOT NULL CHECK(Gender="M" or Gender="F"),
	PRIMARY KEY("MatricNo")
);

CREATE TABLE "Test" (
	"TestID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"Subject"	TEXT NOT NULL,
	"Level"	TEXT NOT NULL,
	"MaxScore"	INTEGER NOT NULL,
	"Year"	INTEGER NOT NULL,
	"Term"	INTEGER NOT NULL,
	"Percentage"	INTEGER NOT NULL
);

CREATE TABLE "Result" (
	"MatricNo"	TEXT,
	"TestID"	INTEGER,
	"Score"	INTEGER NOT NULL,
	FOREIGN KEY("TestID") REFERENCES "Test"("TestID"),
	FOREIGN KEY("MatricNo") REFERENCES "Student"("MatricNo"),
	PRIMARY KEY("MatricNo","TestID")
);


SELECT Student.Class, Student.IndexNo, Student.Name, Test.TestID, Result.Score, Test.MaxScore
FROM Student, Test, Result
WHERE Student.MatricNo = Result.MatricNo AND Test.TestID = Result.TestID
AND Student.Class = "19J08" and Test.Year = "2020" and Test.Subject = "Economics"
ORDER BY Test.TestID ASC, Student.IndexNo ASC