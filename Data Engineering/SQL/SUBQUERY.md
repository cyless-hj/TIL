# SUBQUERY
- 하나의 SQL문 안에 포함된 또다른 SQL
    - SELECT, FROM, WHERE, HAVING

- 서브쿼리의 위치에 따라 이름이 다름
    - SELECT : 스칼라서브쿼리
    - WHERE, HAVING : 서브쿼리

- 서브쿼리로부터 반환되는 RESULTSET의 모양에 따라
    - 단일행
    - 다중행
    - 다중열

1. 부서코드가 노옹철사원과 같은 부서의 직원명단을 조회하시오

```SQL
SELECT DEPT_CODE FROM EMPLOYEE WHERE EMP_NAME = '노옹철';
SELECT * FROM EMPLOYEE WHERE DEPT_CODE = 'D9';
```

- SUBQUERY로 변경

```SQL
SELECT * FROM EMPLOYEE WHERE DEPT_CODE = (SELECT DEPT_CODE FROM EMPLOYEE WHERE EMP_NAME = '노옹철');
```

2. 전 직원 평균 급여보다 많은 급여를 받고 있는 직원의 사번, 이름, 직급코드, 급여를 조회하시오.

```SQL
SELECT EMP_ID, EMP_NAME, JOB_CODE, SALARY FROM EMPLOYEE WHERE (SELECT AVG(SALARY) FROM EMPLOYEE) < SALARY;
```

## 단일행 서브쿼리
- 단일행 서브쿼리, 서브쿼리의 조회 결과 값이 1개인 서브쿼리
- 비교연산자 사용

1. 노옹철 사원의 급여보다 많이 받는 직원의 사번, 이름, 부서, 직급, 급여를 조회


2. 가장 적은 급여를 받는 직원의 사번, 이름, 급여, 부서, 직급, 입사일을 조회


3. 부서별 급여의 합계가 가장 큰 부서를 조회

```SQL
SELECT MAX(SUM(SALARY))
FROM EMPLOYEE
GROUP BY DEPT_CODE;

SELECT DEPT_CODE
FROM EMPLOYEE
GROUP BY DEPT_CODE
HAVING SUM(SALARY) = (SELECT MAX(SUM(SALARY))FROM EMPLOYEE GROUP BY DEPT_CODE);
```

## 다중행 서브쿼리
- 서브쿼리의 조회 결과 값이 여러개 일 때
- IN, ANY, EXISTS 연산자 사용

### IN : 서브쿼리의 결과 값들 중에서 하나라도 일치하는 값이 있으면 TRUE

1. 최고 급여가 499999999원 보다 적은 급여등급을 가지고 있는 직원을 조회하시오

```SQL
SELECT SAL_LEVEL FROM SAL_GRADE WHERE MAX_SAL < 4999999;
SELECT * FROM EMPLOYEE WHERE SAL_LEVEL IN(SELECT SAL_LEVEL FROM SAL_GRADE WHERE MAX_SAL < 4999999);
```

### 비교연산자 ANY : 서브쿼리의 결과 값들 중에서 비교연산의 결과가 하나라도 TURE가 나오면 TRUE
                     WHERE 1 > ANY(SUBQUERY) -> 서브쿼리의 결과값 : [0, 3, 5] TRUE

1. 박나라가 속한 부서의 가장 많은 급여를 받는 사람보다 연봉을 적게 받고
   박나라가 속한 부서에서 가장 적은 급여를 받는 사람보다는 많은 급여를 받는 사원들의 명단을 조회

```SQL
SELECT *
FROM EMPLOYEE
WHERE SALARY < ANY (SELECT SALARY FROM EMPLOYEE WHERE DEPT_CODE =
                            (SELECT DEPT_CODE FROM EMPLOYEE WHERE EMP_NAME = '박나라'))
AND SALARY > ANY (SELECT SALARY FROM EMPLOYEE WHERE DEPT_CODE =
                            (SELECT DEPT_CODE FROM EMPLOYEE WHERE EMP_NAME = '박나라'));
```

### 비교연산자 ALL : 서브쿼리의 결과 값들과 비교연산시 모두 TRUE가 나와야 TRUE
                     WHERE 1 > ALL(SUBQUERY) -> 0, 0.5, 0.7 --> TRUE

1. 박나라가 속한 부서의 사람들 중 가장 많은 급여를 받는 사람보다 더 많은 급여를 받는 직원의 명단을 조회

```SQL
SELECT * 
FROM EMPLOYEE 
WHERE SALARY > ALL(SELECT SALARY FROM EMPLOYEE WHERE DEPT_CODE =
                (SELECT DEPT_CODE FROM EMPLOYEE WHERE EMP_NAME = '박나라'));
```

### EXISTS : SUBQUERY 실행 결과값이 존재하면 TURE 없으면 FALSE
1. 매니저가 존재하지 않는 사원을 조회

```SQL
SELECT * FROM EMPLOYEE E
WHERE NOT EXISTS(SELECT EMP_ID FROM EMPLOYEE WHERE EMP_ID = E.MANAGER_ID);
```

2. 퇴사한 직원과 같은 부서, 같은 직급에 해당하는 사원의 이름, 직급, 부서, 입사일을 조회

```SQL
SELECT EMP_NAME, JOB_CODE, DEPT_CODE, HIRE_DATE
FROM EMPLOYEE
WHERE DEPT_CODE IN (SELECT DEPT_CODE FROM EMPLOYEE WHERE ENT_YN = 'Y')
AND JOB_CODE IN (SELECT JOB_CODE FROM EMPLOYEE WHERE ENT_YN = 'Y');
```

## 다중열 서브쿼리

```SQL
SELECT EMP_NAME, JOB_CODE, DEPT_CODE, HIRE_DATE
FROM EMPLOYEE
WHERE (DEPT_CODE, JOB_CODE) IN (SELECT DEPT_CODE, JOB_CODE FROM EMPLOYEE WHERE ENT_YN = 'Y');
```

## 상(호연)관쿼리
- 상관쿼리는 메인쿼리가 사용하는 컬럼값을 서브쿼리가 이용하는 쿼리
- 메인쿼리의 컬럼값이 변경되면 서브쿼리의 결과값도 바뀐다.

```SQL
SELECT * FROM EMPLOYEE E
WHERE NOT EXISTS(SELECT EMP_ID FROM EMPLOYEE WHERE EMP_ID = E.MANAGER_ID);
```

## 스칼라 서브쿼리
- SELECT 절에서 사용하는 서브쿼리
- 스칼라 서브쿼리는 반드시 달일 값이 반환되어야 한다.

1. 모든 사원의 사번, 이름, 관리자 사번, 관리자명을 조회

```SQL
SELECT EMP_ID, EMP_NAME, MANAGER_ID, (SELECT EMP_NAME FROM EMPLOYEE WHERE EMP_ID = E.MANAGER_ID)
FROM EMPLOYEE E
ORDER BY EMP_NAME DESC;
```

## ROWNUM

```SQL
SELECT ROWNUM, EMP_NAME, SALARY
FROM EMPLOYEE;
```

## 인라인 뷰
- FROM절에 작성하는 서브쿼리
- 서브쿼리의 RESULT SET을 테이블 대신 사용

`. 급여를 많이 받는 상위 5명을 조회

```SQL
SELECT ROWNUM, EMP_NAME, SALARY
FROM
(SELECT EMP_NAME, SALARY
FROM EMPLOYEE
ORDER BY SALARY DESC)
WHERE ROWNUM <= 5;
```