SELECT a1.player_id, a1.event_date AS first_login from Activity a1
JOIN (
	SELECT MIN(event_date) as min_event_date, player_id
    FROM Activity
    GROUP BY player_id
) AS a2 ON a1.event_date = a2.min_event_date AND a1.player_id = a2.player_id



SELECT player_id, MIN(event_date) as first_login
FROM Activity
GROUP BY player_id
