# GROUP BY
- 특정 컬럼을 기준으로 그룹을 만들어 준다.
- group by의 조건절은 having절에서 그룹함수를 사용할 수 있다.
- group 함수 : sum, count, avg, max, min

## GROUP BY 작성법
- group by 컬럼명...

1. 부서별 급여 총액과 평균 급여를 구해보자

```SQL
select dept_code, sum(salary), avg(salary)
from employee
group by dept_code;
```

- 여러 컬럼을 결합해 그룹을 만들기

1. 부서 내 직급별 급여의 합계와 평균을 구해보자

```SQL
select dept_code, job_code, sum(salary), avg(salary)
from employee
group by dept_code, job_code
order by dept_code asc, job_code asc;
```

## EX)
1. 급여가 300만원 이상의 사원들의 부서별 급여 총액을 구해보자

```SQL
select dept_code, sum(salary)
from employee
where salary >= 3000000
group by dept_code;
```

2. 급여의 평균이 300만원 이상인 부서를 조회

```SQL
select dept_code, avg(salary)
from employee
group by dept_code
having avg(salary) >= 3000000;
```

3. 부서 내 직급 내 연봉 레벨 별 급여의 최고 연봉과 최소 연봉을 구하시오
-  구한 뒤 부서를 기준으로 오름차순 정렬하고 NULL값은 아래에 정렬하시오

```SQL
select dept_code, job_code, sal_level, max(salary * 12), min(salary * 12)
from employee
group by dept_code, job_code, sal_level
order by dept_code asc NULLS LAST;
```

<hr>

## 집계 함수 (ROLLUP, CUBE)
- ROLLUP : 그룹 별 중간 집계를 계산
- group by rollup(컬럼, 컬럼, 컬럼)

```SQL
select dept_code, job_code, sal_level, sum(salary)
from employee
group by rollup(dept_code, job_code, sal_level)
order by dept_code asc NULLS LAST;
```

- CUBE
- 그룹으로 지정된 모든 조합에 대한 중간집계를 구한다.

```SQL
select dept_code, job_code, sal_level, sum(salary)
from employee
group by CUBE(dept_code, job_code, sal_level)
order by dept_code asc NULLS LAST;
```