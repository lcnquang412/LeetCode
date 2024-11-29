SELECT name, bonus
FROM 577_Employee
LEFT JOIN 577_Bonus
USING (empId)
WHERE bonus < 1000 or bonus is NULL
