# Hadoop

## Hadoop이란
- 대용량의 데이터 처리 및 저장을 위한 자바 기반의 오픈소스 프레임워크
- 모든 유형의 데이터들의 저장과 처리, 분석이 가능하다.

## Hadoop의 특징
- Hadoop은 2개의 프레임워크로 구성되어 있다.
    1. HDFS
        - Google File System을 기반으로 만든 대용량 분산 저장 / 처리 파일 시스템
        - 장애 복구, 스트리밍 방식의 데이터 접근, 대용량 데이터 저장, 데이터 무결성 보장
        - NameNode와 DataNode를 가지는 Master - Slaver 아키텍쳐
        - Block 구조 파일 시스템
            - 기본적으론 3-Copy 형식으로 분산하여 저장(변경 가능)
            - 예를 들어 200MB의 크기의 데이터를 하나의 블록의 크기를 64MB로 3개로 쪼개서 저장을 한다. 여기서 블록하나의 크기 또한 설정을 바꿀 수 있다.
            - 데이터가 쪼개지고 나서 64MB에 채워지지않아도 하둡은 알아서 64MB에 맞춰 저장한다.
            - 그러면. 하둡을 사용하긴 위해선 자원이 기존보다 3배가 필요하다. 3GB의 데이터가 있으면 저장 공간은 9GB가 있어야하기 때문이다.
            - 현재는 하둡 3버전 등장으로 저장공간이 3배가 필요하진않다. Eraser Coding의 등장으로 저장공간을 절약할 수 있다.
            - 기존에 6개의 데이터를 3개로 복제하여 18블록을 사용했다면, 하둡3은 6개의 데이터의 저장공간과 3개의 패리티를 저장할 공간이 필요하다. (RAID - 스트라이핑 구성)
        - NameNode : 메타데이터 관리, 데이터노드 모니터링, 블록 관리, 클라이언트 요청 접수
        - Secondary NameNode : 체크포인트 노드 (fsimage + edit), 네임스페이스 동기화
        - DataNode : 데이터 저장
    2. MapReduce
        - 하둡의 계산을 담당한다. (HDFS는 하둡의 저장소를 담당)
        - 대용량의 데이터를 처리하기 위한 분산 프로그래밍 모델
        - 정렬된 데이터를 분산처리(Map)하고 이를 다시 합치는(Reduce) 과정을 수행 -> 프로그래머가 직접 작성하는 Map과 Reduce 라는 2개의 메소드로 구성
        - MapReduce Framework를 이용하면 대규모 분산 컴퓨팅 환경에서 대량의 데이터를 병렬로 분석 가능하다.
        - 구성
            - MapReduce는 Hadoop 클러스터의 데이터를 처리하기 위한 시스템으로, 총 2개(Map & Reduce)의 phase로 구성되어 있다.
            - Map과 Reduce사이에는 Shuffle과 Sort라는 스테이지가 존재한다. 각 Map Task는 전체 데이터 세트에 대한 별개의 부분에 대한 작업을 수행하게 되는데, 기본적으로 하나의 HDFS Block을 대상으로 수행하게 된다. 모든 Map Task가 종료되면 -> MapReduce 시스템은 intermediate 데이터를 Reduce phase를 수행할 노드로 분산하여 전송한다.
            - 분산형 파일시스템에서 수행되는
            **① MapReduce 작업이 끝나면 HDFS에 파일이 써지고(write),**
            **② MapReduce 작업이 시작될 때는 HDFS로 부터 파일을 가져오는(Read) 작업이 수행된다.**
        - Map
            - 인풋 데이터를 가공하여 데이터를 연관성 있는 데이터들로 분류하는 작업 -> (key, value)의 형태로 분류
            - 맵 리듀스 Job의 입력 크기를 스플릿이라고 한다. -> 각 스플릿마다 하나의 Map Task를 생성하게 됨 -> 만들어진 Map Task는 스플릿의 레코드를 Map 함수로 처리 -> (key, value) 구조를 가지는 중간 산출물이 생성됨!
        - Reduce
            - Map에서 출력된 데이터에서 중복 데이터를 제거하고 원하는 데이터를 추출(Extract)하는 작업
            - 중간 산출물을 key 기준으로 각 Reduce로 분배 -> 사용자가 정의한 방법으로 각 key의 관련된 정보를 추출하는 단계
            - 중간 산출물을 정렬(Sort)하고 하나로 합쳐 Reduce Task로 생성 -> 사용자 정의 Reduce 함수로 전달 -> 만들어진 결과물은 안정성을 위해 일반적으로 HDFS에 저장!
            - **맵 리듀스의 처리 과정**
                - Input - Splitting - Mapping - Shuffling - Reducing - Final result
                    - Splitting : 문자열 데이터를 라인별로 나눔
                    - Mapping : 라인별로 문자열을 입력 -> (key, value) 형태로 출력
                    - Shuffling : 같은 key를 가지는 데이터끼리 분류
                    - Reducing : 각 key 별로 빈도수를 합산해서 출력
                    - Final Result : 리듀스 메소드의 출력 데이터를 합쳐서 하둡 파일시스템에 저장
        
        - 맵 리듀스의 잡 (Job)
            - Job은 'Full Program' 즉, 전체 프로그램을 의미한다. 데이터 집합을 통해 Mapper와 Reducer를 전체 실행한다. Task는 데이터 조각을 통해 하나의 Mapper 또는 Reducer를 실행하게 된다.
            - 클라이언트가 수행하려는 작업단위로, 입력데이터, 맵리듀스 프로그램, 설정 정보로 구성.
            - 하둡은 Job을 Map Task와 Reduce Task로 작업을 나누어서 실행
            - Job이 실행되는 과정을 제어 해주는 노드
        
        - 맵 리듀스 시스템 구성
            - 맵 리듀스 시스템은 Client, JobTracker, TaskTracker로 구성
            - JobTracker 는 NameNode에 위치
            - TaskTracker 는 DataNode에 위치

            - Client
                - 분석하고자 하는 데이터를 Job의 형태로 JobTracker에게 전달

            - JobTracker
                - NameNode에 위치
                - 하둡 클러스터에 등록된 전체 Job들을 스케줄링하고 모니터링 수행
                - 맵 리듀스 Job들은 JobTracker라는 소프트웨어 데몬에 의해 제어된다. JobTracker들은 마스터 노드에 존재하면 다음과 같은 역할을 수행한다.
                - 클라이언트는 맵리듀스의 Job을 JobTracker에게 보냄 -> JobTracker는 클러스터의 다른 노드들에게 맵과 리듀스 Task를 할당 -> 이 노드들은 TaskTracker라는 소프트웨어 데몬에 의해 각각 실행 -> TaskTracker는 실제로 맵 or 리듀스 Task를 인스턴스화하고, 진행 상황을 JobTracker에게 보고해야함

            - TaskTracker
                - DataNode에서 실행되는 데몬 (DataNode에 위치)
                - 사용자가 설정한 맵리듀스 프로그램을 실행
                - JobTracker로부터 작업을 요청받고, 요청받은 Map과 Reduce 개수만큼 -> Map Task와 Reduce Task를 생성
                - JobTracker에게 상황 보고