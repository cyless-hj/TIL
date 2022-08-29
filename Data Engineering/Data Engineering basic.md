# Data Engineer
- 데이터를 수집 – 가공 – 적재 하는 일을 하는 사람

# 1. Big Data

## 3V / 5V / 7V

1. 3V
- Volume(규모) : 데이터의 크기
- Variety(형태) : 다양한 데이터
- Velocity(속도) : 생산, 처리, 분석 속도

2. 5V
- 3V +
- Veracity(정확성) : 데이터의 품질, 값의 신뢰성
- Value(가치) : 데이터를 통한 가치 창출

3. 7V
- 5V + 
- Validity(타당성) : 목표에 일치하는 데이터
- Volatility(휘발성) : 데이터의 유효기간

## 데이터 처리 과정
수집 → 저장 → 처리 → 탐색 → 분석 → 응용

1. 수집 : 내/외부 데이터 연동 및 통합
2. 저장 : 대용량 / 실시간 데이터 분산 저장
3. 처리 : 데이터 선택, 변환, 통합, 축소
4. 탐색 : 데이터 질의
5. 분석 : 통계 분석
6. 응용 : 시각화

# 2. Hadoop

## Hadoop 이란,
- 대용량 데이터를 분산 저장 및 처리할 수 있는 자바 기반의 오픈소스 프레임워크
- 구글이 논문으로 발표한 Google FileSystem 및 MapReduce 구현
- 여러 대의 서버에 분산되어 있는 데이터를 동시 처리
- 데이터를 복제하여 저장(데이터 유실 시 복구 용이)

## Hadoop Modules
1. Commons : 다른 모듈을 연결 및 지원하는 기본 모듈
2. HDFS : 대용량 데이터 분산 파일 시스템
3. MapReduce : 데이터셋 병렬 처리
4. Yarn : 작업 예약 및 리소스 관리

## HDFS : Hadoop Distributed File System
- Google File System을 기반으로 만든 대용량 분산 저장 / 처리 파일 시스템
- NameNode와 DataNode를 가지는 Master - Slaver 아키텍쳐
- Block 구조 파일 시스템
- NameNode : 메타데이터 관리, 데이터노드 모니터링, 블록 관리, 클라이언트 요청 접수
- Secondary NameNode : 체크포인트 노드 (fsimage + edit), 네임스페이스 동기화
- DataNode : 데이터 저장
- HDFS : 장애 복구, 스트리밍 방식의 데이터 접근, 대용량 데이터 저장, 데이터 무결성

## MapReduce
- 대량의 데이터를 병렬로 분석 -> 분산 처리 지원
- 함수형 프로그래밍 + 분신 컴퓨팅
- 데이터 전송, 분산 병렬 처리 등은 MapReduce Framework가 자동으로 처리 → 개발자는 MapReduce 알고리즘에 맞게 분석 프로그램 개발