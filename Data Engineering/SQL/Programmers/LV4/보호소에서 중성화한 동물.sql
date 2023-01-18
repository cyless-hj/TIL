SELECT ANIMAL_ID, ANIMAL_TYPE, NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O
USING(ANIMAL_ID, ANIMAL_TYPE, NAME)
WHERE SEX_UPON_INTAKE LIKE 'Intact%' AND SEX_UPON_OUTCOME NOT LIKE 'Intact%';