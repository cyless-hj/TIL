SELECT C.NAME AS Customers
FROM Customers C
LEFT JOIN Orders O
ON (C.ID = O.CUSTOMERID)
WHERE CUSTOMERID IS NULL;