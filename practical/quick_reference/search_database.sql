SELECT Student.Class, Student.IndexNo, Student.Name, Test.TestID, Result.Score, Test.MaxScore
FROM Student, Test, Result
WHERE Student.MatricNo = Result.MatricNo AND Test.TestID = Result.TestID
AND Student.Class = "19J08" and Test.Year = "2020" and Test.Subject = "Economics"
ORDER BY Test.TestID ASC, Student.IndexNo ASC;

SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;