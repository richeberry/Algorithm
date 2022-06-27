# Programmers _ Lv2

SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT --datetime에서 시간을 구하려면 hour 사용--
FROM ANIMAL_OUTS 
GROUP BY HOUR(DATETIME) -- hour별로 데이터 정리--
HAVING HOUR >= 9 AND HOUR < 20 -- 9이상 20미만 hour --
ORDER BY HOUR(DATETIME) ASC; -- hour 오름차순으로 정렬--