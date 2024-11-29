SET SQL_SAFE_UPDATES = 0;

DELETE p1
FROM 196_Person p1, 196_Person p2
WHERE p1.email = p2.email and p1.id > p2.id;
