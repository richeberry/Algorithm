# Programmers _ Lv3 _ 헤비 유저가 소유한 장소

SELECT *
FROM PLACES
WHERE HOST_ID IN(SELECT HOST_ID
                FROM PLACES
                GROUP BY HOST_ID
                HAVING COUNT (ID) >= 2)
ORDER BY ID ASC;