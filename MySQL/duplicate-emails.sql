SELECT email AS Email
FROM 182_Person
GROUP BY email
HAVING COUNT(email) > 1;
