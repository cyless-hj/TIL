SELECT DISTINCT CITY
FROM STATION
WHERE REGEXP_LIKE(CITY, '^a|^e|^i|^o|^u','i')
AND REGEXP_LIKE(CITY, 'a$|e$|i$|o$|u$','i');