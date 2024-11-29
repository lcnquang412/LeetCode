SELECT a.name AS Employee
FROM 181_Employee AS a
LEFT JOIN 181_Employee AS b
ON a.managerId = b.id
WHERE a.salary > b.salary;
