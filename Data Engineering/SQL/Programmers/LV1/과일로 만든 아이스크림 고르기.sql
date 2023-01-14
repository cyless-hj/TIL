SELECT FLAVOR
FROM FIRST_HALF F
JOIN ICECREAM_INFO I
USING(FLAVOR)
WHERE F.TOTAL_ORDER > 3000 AND I.INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC;