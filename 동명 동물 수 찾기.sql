# Programmers _ Lv2

SELECT NAME, COUNT(NAME) AS COUNT --COUNT(NAME)의 컬럼명을 COUNT로 변경--
FROM ANIMAL_INS
GROUP BY NAME -- NAME 개수로 구분 --
HAVING COUNT(NAME) >= 2 -- group by에서는 having으로 조건 --
ORDER BY NAME ASC; -- name 오름차순으로 정렬 --