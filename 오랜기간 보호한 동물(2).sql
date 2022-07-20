# Programmers _ Lv3


SELECT INS.ANIMAL_ID, INS.NAME -- 같은 테이블에서 불러와주기 (merge했으니까)
FROM ANIMAL_INS INS, ANIMAL_OUTS OUTS -- 테이블 편하게 명명
WHERE INS.ANIMAL_ID = OUTS.ANIMAL_ID -- 테이블 merge
ORDER BY OUTS.DATETIME - INS.DATETIME DESC -- 보호한 기간
LIMIT 2; -- 위에서부터 제한