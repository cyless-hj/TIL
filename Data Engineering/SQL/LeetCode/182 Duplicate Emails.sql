SELECT EMAIL
FROM Person
GROUP BY EMAIL
HAVING COUNT(*) > 1;