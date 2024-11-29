SELECT customer_number FROM
(
	SELECT customer_number, COUNT(customer_number) AS count_customer_number,
	(
		SELECT MAX(count_customer_number) AS max_customer_number
		FROM (
			SELECT customer_number, COUNT(customer_number) AS count_customer_number
			FROM 586_Orders
			GROUP BY customer_number
		) AS TMP_1
	) AS TMP_2
	FROM 586_Orders
	GROUP BY customer_number
) as TMP_3
WHERE count_customer_number = TMP_2
