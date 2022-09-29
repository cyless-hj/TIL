## TCL (TRANSACTION CONTROL LANGUAGE)
- TRANSACTION : 논리적 최소 작업 단위
- COMMIT / ROLLBACK
- COMMIT : DML에 의해 변경된 테이블 상태를 완전히 반영
- ROLLBACK : 이전 COMMIT 상태로 테이블 상태를 되돌림
- DDL이 자동 COMMIT이기 때문에, DML을 작성하고 DDL을 이어서 작성하면, 앞의 DML이 COMMIT된다.
