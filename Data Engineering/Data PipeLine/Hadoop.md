# Hadoop

## Hadoop이란
- 대용량의 데이터 처리 및 저장을 위한 자바 기반의 오픈소스 프레임워크
- 모든 유형의 데이터들의 저장과 처리, 분석이 가능하다.
![맵리듀스](https://user-images.githubusercontent.com/75618206/215367257-2828282d-9fb6-4eda-a8ab-8818f85d3b80.png)

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

## Hadoop 튜닝

### 맵리듀스 잡 영향 설정
- 블록 크기 설정
    - 블록 크기를 크게 설정해 리플리케이션(Replication) 위치 변경에 드는 비용을 줄일 수 있으며, 작업량도 줄여 처리 시간을 단축할 수 있다. hdfs-site.xml의 dfs.blocksize 기본 블록 크기는 64MB이지만, 일반적으로 128MB로 설정한다. 더 크게 하면 성능이 올라갈 것 같지만, 블록 크기는 NameNode 힙 메모리에 영향을 준다는 사실을 염두에 둬야 한다.

- 리플리케이션 수 설정
    - 하둡의 일반적인 리플리케이션 수는 3이다. 하지만 클러스터 크기에 따라서 2도 사용한다. 만일 클러스터 크기가 충분하다면 복제계수를 조금 더 늘리는 것도 좋은 방법이다. 왜냐하면 맵리듀스 코드는 각 하둡 클러스터에 분산 복제되므로 자신의 코드 중 해당 데이터 노드에 맞는 데이터가 있다면 성능이 좋아지기 때문이다. 하지만 맵과 리듀서 사이에는 항상 임시 데이터를 생성하게 되는데, 그 데이터도 복제 계수가 3이 과하다면 dfs.replication 값을 1이나 2로 조정한다.

- 태스크를 실행하는 CHILD 프로세스 재사용
    - child는 맵태스크나 리듀스태스크를 실행하면 생성되는 독립적인 프로세스다. child 프로세스를 생성했다가 처리가 완료되면 종료한다. 따라서 이 child 프로세스를 재사용해 프로세스 생성과 제거에 드는 시간을 줄일 수 있다. mapred.job.reuse.jvm.num.tasks 속성을 이용하고 기본 값은 1이으므로 태스크를 한 번 실행한 후 프로세스를 제거한다. 0으로 설정하면 잡이 완료되기까지 child 프로세스를 사용하며, 2이상 설정하면 하나의 프로세스에서 설정한 태스크 수만큼 재사용하게 된다.

- 리듀스 단계 시작 시점 제어
    - 리듀스 단계는 맵 단계가 5% 완료된 시점에서 시작된다. 맵 단계가 완료된 후 리듀스 단계를 시작하는 것보다 중간에 임시 데이터가 생성되는 시점에 시작하는 것이 효율적일 것이다. 하지만 5%라고 해도 중간 데이터가 너무 적으면 처리 작업을 진행하지 않는다. 그렇기 때문에 주기적으로 체크하게 되고 이로 인해 비용이 발생하게 되므로 리듀스 단계를 늦추는 것이 효율적일 때가 있다. mapredsite.xml에서 mapred.reduce.slowstart.completed.maps 속성을 사용하고 1은 100%를 의미한다. 이 경우 맵 단계가 모두 완료되고 리듀스 단계를 시작한다는 의미다. 일반적으로 0.3(30%)에서 0.9(90%) 사이에서 선택하는 것이 좋다.

### 맵 태스크 튜닝
- 매퍼 코드의 마지막은 Context 객체에 키와 밸류를 전달해 마무리한다. Context 객체는 버퍼에 있는 데이터를 관리한다. 만일 밸류 값이 매우 크면 어떻게 될까? 그 때는 아마 OOM(Out Of Memory)이 발생할 것이다. 그래서 하둡은 이때의 데이터 일부를 디스크에 작성한다. [그림 Ⅲ-1-8]에서 셔플링 전의 그림을 보면, 디스크에 데이터를 쓰는 것을 확인할 수 있다. 그리고 맵 태스크는 이런 데이터를 반복 병합처리하는 것이다. 결국 맵 태스크에서는 데이터를 처리하고 결과를 디스크에 쓰면 추후 http를 통해 리듀서가 가져간다. 이 시점에 튜닝 포인트는 메모리 관리와 병합처리 속도다.

- 데이터 저장 메모리 튜닝
    - 메모리 튜닝으로 io.sort.mb 값을 늘린다. 기본 값은 100MB다. io.sort.record.percent를 설정한다. 기본 값은 0.05(5%)다. io.sort.spill.percent 값을 조정한다. 기본 값은 0.8(80%)이다. 그러면 데이터영역과 레코드 등의 영역 버퍼 크기를 계산해 보자.

    - io.sort.mb 기본 값이 100mb라면, io.sort.record.percen 레코드, 데이터 영역 할당 용량 결정
    - 레코드 용량 = (int)(전체 버퍼 크기 x io.sort.record.percent)
    - 레코드 용량2 = 레코등 용량 ? (레코드 용량 %16)
    - 데이터 영역용 버퍼 크기 = io.sort.mb / 레코드 용량2
    - 데이터를 유지할 수 있는 메모리의 크기 = 레코드 용량2 / 16

- 데이터 병합
    - io.sort.factor 속성 값을 조정한다. 기본 값은 100이다. 조각난 데이터 크기를 늘리면 속도는 크게 느려지므로 100~200 사이에서 조정하는 것이 좋다.

### 리듀스 태스크 튜닝
- 맵 태스크는 결과를 디스크에 저장하고 리듀스 태스크가 원격지에 http를 통해 데이터를 복사해 간다. 이때 복사를 해가는 리듀스 태스크의 스레드 수를 늘리면 조금 빨리 가져갈 수 있다. mapred.reduce.parallel.copies를 설정해 스레드 수를 조정한다. 기본 값은 5다.
- 리듀스 태스크도 많은 튜닝 포인트가 있지만, 핵심은 셔플링을 줄이거나 셔플링 처리 속도를 높이는데 있다. 이것은 버퍼(메모리) 크기가 포인트가 되는데, 버퍼의 크기는 Java VM에 영향을 준다. 하둡의 Java VM은 하둡 전체 클러스터의 영향도이기 때문에 섹션 범위를 벗어나므로 관련 책이나 웹사이트를 확인하기 바란다. 하둡2.X에서는 지금까지 옵션의 이름이 바뀌었으므로 꼭 확인한다. http://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/mapreddefault.xml에서 맵리듀스 설정 값을 확인할 수 있다.
- 이 절에서는 하둡 맵리듀스 튜닝에 대해 살펴보았다. 하둡 전체 튜닝은 아니지만, 하둡 맵리듀스에 대한 이해만으로도 튜닝할 수 있을 것이다. 물론 맵리듀스는 애플리케이션이기 때문에 애플리케이션에서 성능이 나아지지 않으면 클러스터 튜닝을 해야 한다. 이 때 JavaVM, HDFS 등을 튜닝해야 하고, 이 조차도 성능이 나아지지 않으면 시스템 튜닝 차원에서 OS와 네트워크 튜닝을 해야 한다. 또한 하둡은 데이터 처리 관점에서만 보면 데이터 노드가 증설될수록 성능은 선형적으로 늘어난다.
- 데이터 처리는 다양한 프레임워크가 존재한다. 하둡 에코시스템에서는 Pig와 Hive를 가장 많이 사용하고 있다. 하지만 네이티브 레벨에서 성능 위주의 배치 처리와 함께 특성에 따라서 다루기 힘든 Geospatial 데이터를 다룰 때는 맵리듀스가 더 적절할 수 있다. 하지만 맵리듀스는 학습곡선이 분명하게 존재하는 프로그래밍 방법론이자 패러다임이다. 그래서 최근에는 맵리듀스 처리를 쉽게 할 수 있는 프레임워크가 따로 존재한다. Apache Crunch, Cascading 등이 그것이다. 자바를 모르면 파이썬과 R로 맵리듀스를 사용할 수도 있다. 그리고 맵리듀스는 어떻게 보면 하둡을 더 자세하게 이해하기 위한 첫 번째 선택이 될 수 있다.
