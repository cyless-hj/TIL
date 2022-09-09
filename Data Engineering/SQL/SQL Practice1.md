# SQL Practice

1. 
```SQL
select department_name "학과 명", category 계열 from TB_DEPARTMENT;
```
2. 
```SQL
select department_name || '의 정원은 ' || capacity || '명 입니다.' "학과별 정원" from TB_DEPARTMENT;
```

3. 
```SQL
select department_no from tb_department where department_name = '국어국문학과';

select student_name from tb_student where department_no = 001 and student_ssn like '%2______' and absence_yn = 'Y';

select student_name 
from tb_student 
where department_no = (select department_no from tb_department where department_name = '국어국문학과') 
and student_ssn like '%2______' and absence_yn = 'Y';
```

4. 
```SQL
select student_name from tb_student where student_no in ('A513079', 'A513090', 'A513091', 'A513110', 'A513119');
```

5. 
```SQL
select department_name, category from tb_department where capacity BETWEEN 20 and 30;
```

6. 
```SQL
select professor_name from tb_professor where department_no is null;
```

7. 
```SQL
select * from tb_student where department_no is NULL;
```

8. 
```SQL
select class_no from tb_class where preattending_class_no is not null;
```

9. 
```SQL
select distinct category from tb_department;
```

10. 
```SQL
select student_no, student_name, student_ssn 
from tb_student 
where entrance_date like '02%' and student_address like '전주시%' and absence_yn = 'N';

select student_no, student_name, student_ssn 
from tb_student 
where entrance_date between '02/01/01' and '02/12/31' and student_address like '전주시%' and absence_yn = 'N';
```