SELECT w1.id
FROM Weather w1, Weather w2
WHERE w1.temperature > w2.temperature AND DATE(DATE_ADD(w1.recordDate, INTERVAL -1 DAY)) = w2.recordDate;
