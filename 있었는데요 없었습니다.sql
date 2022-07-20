# Programmers _ Lv3 _ 있었는데요 없었습니다

SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I LEFT JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.DATETIME > O.DATETIME -- 입양된 날짜가 보호소에 들어온 날짜보다 먼저이면 = 보호소에 들어온 날짜가 입양된 날짜보다 크면
ORDER BY I.DATETIME ASC;