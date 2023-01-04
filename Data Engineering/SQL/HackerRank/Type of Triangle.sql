SELECT
    CASE WHEN A + B <= C OR A + c < B OR B + C <= A THEN 'Not A Triangle'
    WHEN A = B AND B = C AND C = A THEN 'Equilateral'
    WHEN A = B OR B = C OR C = A THEN 'Isosceles'
    ELSE 'Scalene'
    END
FROM TRIANGLES;