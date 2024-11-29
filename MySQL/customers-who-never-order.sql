SELECT c.name as Customers
FROM 183_Customers AS C
LEFT JOIN 183_Orders AS O
ON C.id = O.customerId
WHERE O.id IS NULL;
