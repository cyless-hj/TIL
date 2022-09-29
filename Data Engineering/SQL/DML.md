# DML
- 데이터 조작어(Data Manipulation Language)
- 테이블에 값을 추가하거나(INSERT) 수정하거나(UPDATE) 삭제(DELETE)

## INSERT
- 새로운 행을 추가하는 구문
- INSERT INTO 테이블명(컬럼명, 컬럼명2...) VALUES(데이터1, 데이터2...)
- 컬럼을 지정하지 않으면 NULL이 들어간다
- 모든 컬럼에 값을 넣는 구문일 경우 컬럼명은 생략이 가능하다.
- INSERT INTO 테이블명 VALUES(데이터1, 테이터2...)

```SQL
INSERT INTO jhj_emp(EID, PHONE, HIRE_DATE, ENO, ENAME, MARRIAGE, AGE)
VALUES(0, '010-0000-4141', '2022-09-29', '000000-1111111', 'JHJ', 'N', 21);

-- 서브쿼리로 데이터 입력하기
CREATE TABLE JHJ_EMP_DEPT(
    EMP_ID NUMBER,
    EMP_NAME VARCHAR2(30 CHAR),
    DEPT_TITLE VARCHAR2(30 CHAR)
);

INSERT INTO JHJ_EMP_DEPT(
    SELECT EMP_ID, EMP_NAME, DEPT_TITLE
    FROM EMPLOYEE
    LEFT JOIN DEPARTMENT ON(DEPT_CODE = DEPT_ID)
);
```
<hr>

## UPDATE
- 수정
- UPDATE 테이블명 SET 컬럼명 = 변경할 값, ... (WHERE절);

```SQL
UPDATE JHJ_EMP_DEPT SET DEPT_TITLE = '인사잘함부' WHERE EMP_NAME = '전지연';

UPDATE JHJ_EMP_DEPT 
SET DEPT_TITLE = (SELECT DEPT_CODE FROM EMPLOYEE WHERE EMP_NAME = '전지연')
WHERE EMP_NAME = '전지연';
```
<hr>

## DELETE
- 테이블의 행을 삭제하는 구문
- WHERE절을 지정하지 않으면 모든 데이터가 사라진다.
- DELETE FROM 테이블명 WHERE 조건식

<br>

- JHJ_EMP_DEPT 전지연 삭제하기

```SQL
DELETE JHJ_EMP_DEPT WHERE EMP_NAME = '전지연';
```

<hr>

## TRUNCATE
- 테이블 전체 행 삭제
- 장점 : 빠르다
- 단점 : ROLLBACK이 안된다.

```SQL
TRUNCATE TABLE JHJ_EMP_DEPT;
```