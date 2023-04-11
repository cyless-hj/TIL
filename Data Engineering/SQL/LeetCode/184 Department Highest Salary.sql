SELECT D.NAME AS DEPARTMENT, E.NAME AS EMPLOYEE, E.SALARY AS SALARY
FROM Employee E
JOIN (SELECT departmentId, MAX(salary) AS MAX_SALARY
      FROM EMPLOYEE
      GROUP BY departmentId) E2
ON E.departmentId = E2.departmentId
JOIN Department D
ON E.departmentId = D.ID
WHERE E.salary = E2.MAX_salary;