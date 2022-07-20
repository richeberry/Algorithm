# Programmers _ Lv3


SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
-- LEFT JOIN했으므로 I 기준으로 select
FROM ANIMAL_INS I LEFT JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
-- ANIMAL_INS 를 I로, ANIMAL_OUTS를 O로 테이블 이름을 바꾸고 같은 컬럼 ANIMAL_ID를 중심으로 I에 O를 LEFT JOIN
WHERE I.SEX_UPON_INTAKE LIKE "Intact%" AND (O.SEX_UPON_OUTCOME LIKE "Spayed%" OR O.SEX_UPON_OUTCOME LIKE "Neutered%")
-- 보호소 들어올 때: 미중성화 - Intact로 시작하는 데이터명
-- 보호소를 나갈 때: 중성화 - Spayed 또는 Neutered로 시작하는 데이터명
ORDER BY I.ANIMAL_ID ASC;
-- ANIMAL_ID 기준 오름차순으로 정렬