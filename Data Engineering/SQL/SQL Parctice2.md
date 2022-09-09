# SQL Practice

1. 이름에 '형'이 들어가는 사원의 사원ID, 사원이름, 직업명을 출력하세요 

```SQL
select e.emp_id, e.emp_name, j.job_name 
from employee e 
inner join job j
on(e.job_code = j.job_code)
where e.emp_name like '%형%';
```

2. 부서명이 D5, D6 인 사원의 이름, 직업명, 부서코드, 부서명을 출력하세요

```SQL
select e.emp_name, d.dept_id, d.dept_title 
from employee e 
inner join department d
on(e.dept_code = d.dept_id)
where d.dept_id in ('D5', 'D6');
```

3. 부서가 위치한 국가가 한국이나 일본인 사원의
- 이름, 부서명, 지역명, 국가명을 출력하시오
- employee, department, location, national 

```SQL
select emp_name, dept_title, local_name, national_name
from employee e
inner join department d on(e.dept_code = d.dept_id)
inner join location l on (d.location_id = l.local_code)
inner join national n on (l.national_code = n.national_code)
where national_name in ('한국', '일본');
```

4. EMPLOYEE 테이블에서 전화번호 처음 3자리가 010이 아닌 사원의 이름, 전화번호 조회하시오

```SQL
select emp_name, phone 
from employee
where phone not like '010%';
```

5. 사번, 사원명, 급여, 구분 컬럼을 출력하시오
- 구분 컬럼은
- 급여가 500만원 이상이면 '고급'
- 급여가 300~500만원이면 '중급'
- 그 이하는 '초급'으로 출력처리 하도록 작성하시오

```SQL
select emp_id 사번, emp_name 사원명, salary 급여,
        case when salary >= 5000000 then '고급'
             when (salary < 5000000) and (salary >= 3000000) then '중급'
             else '초급'
        end 구분
from employee;
```

6. EMPLOYEE 테이블에서 메일주소 '_'의 앞이 4글자 이면서 DEPT_CODE가 D9 또는 D6이고 고용일이 90/01/01 ~ 00/12/01 이면서 급여가 270만원 이상인 사원의 전체 정보를 조회하시오

```SQL
select * 
from employee
where email like '____$_%' escape '$' 
and dept_code in ('D9', 'D6') 
and hire_date between '90/01/01' and '00/12/01' 
and salary >= 2700000;
```

7. 부서별 그룹의 급여합계가 9백만원을 초과하는 부서의 부서코드와 급여합계를 조회하고 부서코드 내림차순으로 정렬하시오

```SQL
select dept_code, sum(salary)
from employee
group by dept_code
having sum(salary) > 9000000
order by dept_code desc;
```

8. 70년대 생이면서 성별이 여성이고 성이 전씨인 사원의 이름, 주민등록번호, 부서명, 직업명을 출력하세요.

```SQL
select emp_name, emp_no, d.dept_title, j.job_name
from employee e
inner join department d
on (e.dept_code = d.dept_id)
inner join job j
using (job_code)
where emp_no like '7%'
and emp_no like '%2______'
and emp_name like '전%';
```

9. 퇴사한 사람과 퇴사하지 않은 사람의 숫자를 출력하세요

```SQL
select count(emp_id)
from employee
group by ent_yn;
```

10. 자신의 매니저보다 급여가 더 높은 사원의 이름, 부서, 급여, 매니저 이름, 매니저 부서, 매니저 급여를 조회하시오

```SQL
select e.emp_name, e.dept_code, e.salary, m.emp_name, m.dept_code, m.salary
from employee e
inner join employee m
on(e.manager_id = m.emp_id)
where e.salary > m.salary;
```

11. 부서가 위치한 국가별 평균 급여를 조회하시오, 
- 만약 해당 국가에 있는 부서가 존재하지 않더라도 국가 정보는 출력되도록 작성하시오

```SQL
select n.national_name, d.dept_title, avg(e.salary)
from employee e
inner join department d on(e.dept_code = d.dept_id)
inner join location l on (d.location_id = l.local_code)
inner join national n on (l.national_code = n.national_code)
group by n.national_name, d.dept_title;
```