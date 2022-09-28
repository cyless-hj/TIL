# SQL Function

## 1. 문자 관련 함수
- LENGTH, LENGTHB, SUBSTR, INSTR, CONCAT, REPLACE, TRIM, LPAD, RPAD

### 1. LENGTH : 문자열의 길이 반환

```SQL
select length('oracle') from dual; --> dual : 가상 테이블
select length('오라클') from dual;
```

### 2. LENGTHB : 문자열의 바이트 길이 반환

```SQL
select lengthb('oracle') from dual;
select lengthb('오라클') from dual;
```

### 3. SUBSTR : 문자열 슬라이싱

```SQL
select substr('PCLASS', 2) from dual;
select substr('PCLASS', 2, 3) from dual;
```

### 4. INSTR : 문자열 인덱스 반환(오라클은 인덱스 값이 1부터 시작)

```SQL
select instr('AABAACAABBAA', 'B') from dual;
select instr('AABAACAABBAA', 'B', 4) from dual;
select instr('AABAACAABBAA', 'B', -1, 3) from dual;
```

### 5. CONCAT : 문자열 합치기

```SQL
select concat('A', 'B') from dual;
select 'A' || 'B' from dual;
```

### 6. REPLACE : 문자열 대체

```SQL
select replace('서울시 강남구 선릉동', '선릉') from dual;
select replace('서울시 강남구 선릉동', '선릉동', '역삼동') from dual;
```

### 7. TRIM : 양쪽 공백 제거

```SQL
select trim('  multicampus   ') from dual;
select trim('m' from 'multicampus   ') from dual; -->제일 앞에 m이 있을 때만 제거
select trim(trailing 's' from 'multicampus') from dual;
select trim(both 'm' from 'multicampus') from dual;
```

### 8. LPAD : 특정 문자를 채워 길이를 맞춰준다

```SQL
select lpad(email, 20) from employee;
select rpad(email, 20, '#') from employee;
```

### ex) EMPLOYEE 테이블에서 사원명과 주민번호를 조회하세요
        - 단 주민번호는 생년월일과 '-' 까지만 보이게 하고 나머지 자리의 숫자들은 *로 바꾸어 출력하세요.

```SQL
select emp_name, rpad(substr(emp_no, 1, 7), 14, '*') from employee;
select emp_name, replace(emp_no, substr(emp_no, 8), '*******') from employee;
```
<hr>

## 2. 숫자 처리 함수
- ABS, MOD, ROUND, FLOOR, TRUNC, CEIL

<hr>

## 3. 날짜 처리 함수
- SYSDATE, MONTHS_BETWEEN, ADD_MONTHS, EXTRACT

### 1. SYSDATE : 시스템에 저장되어있는 현재 날짜

```SQL
select sysdate from dual;
```

### 2. SYSTIMESTAMP : 현재 세계 표준 날짜, 시간

```SQL
select systimestamp from dual;
```

### 3. LOCALTIMESTAMP : 현재 날짜, 시간

```SQL
select localtimestamp from dual;
```

### 4. MONTHS_BETWEEN : 두 날짜 사이 개월 수 반환
- 사원들의 근무 개월 수를 구해보도록 하자

```SQL
select emp_name, trunc(months_between(sysdate, hire_date)) as "근무 개월수" 
from employee 
order by hire_date asc;
```

### 5. ADD_MONTHS : 개월 수 더한 날짜 반환

```SQL
select emp_name, hire_date, add_months(hire_date, 12) from employee;
```

### 6. EXTRACT : 날짜의 원하는 값 추출

```SQL
select emp_name, 
extract(year from hire_date), 
extract(month from hire_date), 
extract(day from hire_date)
from employee;
```

<hr>

## 4. 형변환 함수
- TO_CHAR, TO_DATE

### 1. TO_CHAR

```SQL
select to_char(sysdate, 'year') from dual;
select to_char(sysdate, 'year"년"') from dual;
select to_char(sysdate, 'yyyy"년"') from dual;
select to_char(sysdate, 'yyyy"년 " month DD "일"') from dual;
select to_char(123456789, '9,999,999,999') from dual;
select to_char(10000, '$99999') from dual;
select to_char(10000, 'L99999') from dual;
select to_char(10000, 'L99,999') from dual;
```

<hr>

## 5. null 처리 함수
- null : 아직 정해지지 않은 값
- null의 산술연산이나 비교연산의 결과는 null
- null의 논리연산 확인
- NVL, NVL2, NULLIF

### 1. NVL : null 값을 대체

```SQL
select emp_name, bonus, nvl(bonus, 0) from employee;
select emp_name, dept_code, nvl(dept_code, '무소속') from employee;
```
### 2. NVL2 : null 여부에 따라 값 반환
- employee 테이블에서 보너스가 null 인 직원은 50%, 아닌 직원은 10% 준다.

```SQL
select emp_name, bonus, nvl2(bonus, 0.5, 0.1) from employee;
```

### 3. NULLIF : 두 값이 동일하면 null을 반환

```SQL
select nullif('1234', '123') from dual;
select nullif('1234', '1234') from dual;
```
<hr>

## 6. 선택 함수 DECODE
- case when then 기능을 하는 함수
- 주민등록번호 뒷자리의 첫 자리가 홀수이면 남자, 짝수이면 여자로 표시하시오.

```SQL
select emp_name, emp_no, decode(mod(substr(emp_no, 8, 1), 2), 1, '남', 0, '여')
from employee;
```