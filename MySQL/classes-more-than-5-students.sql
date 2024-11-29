SELECT class FROM
(SELECT COUNT(class) as classCount, class
FROM 596_Courses
GROUP BY class
) AS TMP
WHERE classCount >= 5;
