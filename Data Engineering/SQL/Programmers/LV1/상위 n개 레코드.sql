SELECT NAME
FROM (SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY DATETIME)
WHERE ROWNUM = 1;