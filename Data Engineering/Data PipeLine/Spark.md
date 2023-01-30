# Spark
- 대규모 데이터 처리를 위한 통합 분석 엔진
- 하둡의 HDFS는 DISK I/O를 기반으로 동작하는데 현대 it기술로 진입하면서 DISK I/O의 빅데이터 처리 방식으로는 실시간성의 데이터를 처리하지 못하게 되었다.
- 따라서 Hadoop이 속도가 느린 것을 해결하기 위해 Spark 사용
- Disk I/O가 아닌 인메모리로 처리

## Spark 처리방식
![Spark](https://user-images.githubusercontent.com/75618206/215367008-bac70185-aa65-4c99-9504-11887ea3b306.png)

### Spark Cluster
- Driver Program : 우리가 작업하는 환경을 뜻한다 Script(java,python,scala)를 작성하는 것이라고 보면된다.
- Cluster Manager : 위에 작업한 script 내용을 실행 시키면 cluster manager가 worker node에게 일을 분배하여 처리 하게 해준다. (ex: Hadoop-yarn, aws-Eleatic MapReduce 등)
- Worker Node : Worker Node는 1CPU 하나당 1Node가 배치되어 인메모리 연산을 진행한다.
- spark는 Driver Program, Cluster Manager, Workder Node로 구성 되어 있다. 위와 같은 이유 때문에 인메모리 연산 분산 처리가 가능해져 속도가 빨라지게 되었다. 즉 Spark는 Cluster Manager가 Workder node를 알아서 CPU 로 할당하여 분산 처리를 하기 때문에 연산 속도가 빨라 졌다고 한다.

### Spark 구성
- Spark는 SQL, Streaming, MLlib, GraphX등을 사용하여 연산을 처리 할 수 있다.
    - Spark Core
    - Spark SQL
    - Spark Streaming
    - MLlib
    - GraphX

### Spark Job의 구성
- Spark Submit job이나 jar파일 같이 실행 하게 되면 아래의 형식으로 구성되어 진행 되게 된다.
- spark-Submit을 하게 되면 Job으로 Cluster Manager에게 할당되게 되고 
- Stage별로 작업을 나눈다음 
- Stage별로 들어갈 용량 및 작업량을 파악 하여 Executor에서 Task를 진행한다.
- 그리고 그 결과값을 Cluster Manager에게 Cluster Manager는 다시 Driver Program에 전달한다.
![saprk job](https://user-images.githubusercontent.com/75618206/215367021-4ef93419-d374-43e3-b8d9-a92ba191b6e2.png)

### Partition이란?
- RDDs나 Dataset를 구성하고 있는 최소 단위 객체이며, 스파크의 성능과 리소스 점유량을 크게 좌우할 수 있는 RDD의 가장 기본적인 개념입니다.
- 데이터 파티셔닝은 데이터를 여러 클러스터 노드로 분할하는 메커니즘을 의미합니다.
- 각 Partition은 서로 다른 노드에서 분산 처리됩니다.즉, 1 Core = 1 Task = 1 Partition입니다. 
- Spark에서는 하나의 최소 연산을 Task라고 표현하는데, 이 하나의 Task에서 하나의 Partition이 처리됩니다. 또한, 하나의 Task는 하나의 Core가 연산 처리합니다.
- 이처럼 설정된 Partition 수에 따라 각 Partition의 크기가 결정됩니다. 그리고 이 Partition의 크기가 결국 Core 당 필요한 메모리 크기를 결정하게 됩니다.
    - Partition 수 → Core 수
    - Partition 크기 → 메모리 크기
- 따라서, Partition의 크기와 수가 Spark 성능에 큰 영향을 미치는데, 통상적으로는 Partition의 크기가 클수록 메모리가 더 필요하고, Partition의 수가 많을수록 Core가 더 필요합니다.
    - 적은 수의 Partition = 크기가 큰 Partition
    - 많은 수의 Partition = 크기가 작은 Partition
- 즉, Partition의 수를 늘리는 것은 Task 당 필요한 메모리를 줄이고 병렬화의 정도를 늘립니다.

#### Partition의 종류
- 동일한 Partition이지만 쓰이는 때에 따라 분류를 합니다.
    - Input Partition
    - Output Partition
    - Shuffle Partition

- spark.conf.set("spark.sql.files.maxPartitionBytes",bytes)
    - 처음 파일을 읽을 때 생성하는 파티션
    - 기본값은 134217728(128MB)
    - 파일(HDFS상의 마지막 경로에 존재하는 파일)의 크기가 128MB보다 크다면 Spark에서 128MB만큼 쪼개면서 파일을 읽는다.
    - 파일의 크기가 128MB보다 작다면 그대로 읽어 들여, 파일 하나당 Partition하나가 된다.
    - file-based sources인 JSON,parquet,ORC 같은 것에만 적용된다.

- spark.conf.set("spark.sql.shuffle.partitions",num of partition)
    - spark.sql.shuffle.partitions 옵션은 join,groupBy 혹은 aggregation 같은 연산을 할 시 data shuffling되는 파티션 수를 나타냅니다.
    - 파티션의 개수는 default로는 200으로 지정 되어 있으며, spark.conf.set("spark.sql.shuffle.partitions", 1800)와 같은 형태로 조정이 가능합니다.
    - Core 수에 맞게 설정하라고 하기보단, Partition의 크기에 맞추어서 설정
    - Partition의 크기가 크고 연산에 쓰이는 메모리가 부족하다면 Shuffle Spill(데이터를 직렬화하고 스토리지에 저장, 처리 이후에는 역 직렬 화하고 연산 재개함)이 일어남 -> Task가 지연되고 에러가 발생 -> 하둡클러스터에 에러가 나고 spark 강제종료
    - Memory Limit Over와 같이, Shuffle Spill도 메모리 부족으로 나타나는데, 보통 이에 대한 대응을 Core 당 메모리를 늘리는 것으로 해결
    - 일반적으로, 하나의 Shuffle Partition 크기가 100~200MB정도 나올 수 있도록 수를 조절하는 것이 최적
    - 클러스터의 익스큐터 수보다 파티션의 수를 더 크게 지정하는 것이 대체로 좋다. executor num > partition num
    - 로컬 머신에서 처리할 경우 병렬로 처리할 수 있는 task가 제한적이므로 이 값을 작게 설정

- coalesce(), repartition()은 언제 사용하는지?
    - filter()와 같은 transformation 연산을 수행하다 보면 최초에 설정된 파티션 개수가 적합하지 않은 경우가 있는데, 이럴 때 파티션 수를 조정하는 option을 사용합니다.
    - 파일을 저장할 때 생성하는 Partition, 이 Partition의 수가 HDFS 상의 마지막 경로의 파일 수를 지정
    - 보통 groupBy 집계 후 저장할 때 데이터의 크기가 작아짐 -> spark.sql.shuffle.partitions 설정에 따라 파일 수가 지정되는데, 이때 파일의 크기를 늘리기 위해 repartition와 coalesce을 사용해 Partition 수를 줄임으로서 파일의 크기를 늘림
    - df.where()를 통해 필터링을 하고 나서 그대로 저장한다면 파편화가 생김 -> repartition(cnt) (셔플)을 한 후 저장

- coalesce() vs repartition()
    - 이 2개의 가장 큰 차이는 셔플을 하냐 안하냐의 차이입니다(default로 봤을 때)
    - coalesce는 파티션을 줄일 때 사용하고, repartition()은 파티션 수를 늘리거나 줄일 때 사용합니다.
    - coalesce(numofpartition,true) 처럼 true 옵션을 줬을 때에는 강제로 셔플을 할 수 있습니다. -> true옵션을 주게 되면 파티션을 늘릴 수도 있습니다.
    - default값으로 사용하려면 파티션 수를 줄일 땐 coalesce(), 파티션 수를 늘릴 땐 repartition()사용

- spark.conf.set("spark.sql.files.maxRecordsPerFile",num of records)
    - spark write시에 파일의 record수를 지정하여 해당 record수 별로 파일을 생성 할 수 있는 config
    - write시에 .option("maxRecordsPerFile",100000) 으로도 지정 가능

## Spark Shuffle
- 파티션간 물리적인 데이터 이동
- Shuffle 은 Spark 에서 데이터를 재분배하는 방법

- Shuffle 을 이해하기 위해서는, reduceByKey 의 작동 방식을 알아야합니다.
- reduceByKey 는 동일한 Key 를 가지고 있는, 모든 record 값을 취합하는 작업입니다.
    - (A, 1), (A, 2), (A, 3) → (A, 6)
- 하지만, Spark 의 분산처리는 파티션 단위로 진행되기 때문에, 동일한 Key 의 모든 record 값을 취합하기 위해선, 동일한 Key 를 가진 튜플 데이터가 전부 같은 파티션에 있어야합니다.
- 따라서, 모든 튜플 데이터가 여러 클러스터에 분산 저장되어 있을 때, 동일한 Key 를 가진 튜플 데이터를 동일한 파티션에 두기 위해, 데이터의 위치를 재조정하는 방법이 Shuffle 입니다.

- 변환 함수의 경우 각 파티션 별로 값을 (부분적으로) 병합할 수 있으나 병합 함수는 여러 파티션의 값을 최종 병합하므로, 셔플링이 수행된다.
- 중간 파일을 기록, 읽으면서 오버헤드 발생 + 네트워크로 셔플링할 데이터 전송하므로 셔플링 횟수는 최대한 줄여야함
    - partitioner를 명시적으로 변경하는 경우
    - Partitioner를 제거하는 경우
        **- ※ map, flatmap은 RDD의 partitioner를 제거하는 연산임** (정확히는 그 뒤에 특정 변환 연산자를 사용할 경우)

## DataSet

### DataSet 개념
- DataSet은 구조적 api 의 기본 데이터타입입니다. DataFrame 또한 row 타입의 DataSet 입니다. 그리고, 스파크가 지원하는 다양한 언어에서 사용할 수 있습니다.
- DataSet 의 경우는 jvm 을 이용하는 언어인 스칼라와 자바에서만 사용할 수 있습니다. DataSet을 이용해 DataSet의 각 로우를 구성하는 객체를 정의합니다.
    - 스칼라에서는 스키마가 정의된 케이스 클래스 객체를 이용해 DataSet을 정의합니다.
    - 자바에서는 자바빈 객체를 이용해 DataSet을 정의합니다.
- 도메인별 특정 객체를 효과적으로 지원하기 위해 인코더(encoder) 라 불리는 특수 개념이 필요합니다.
- 인코더는 도메인별 특정 객체 T 를 스파크 내부 데이터타입으로 매핑하는 시스템을 의미합니다.
- 예를 들어, name(string)과 age(int)두 개의 필드를 가진 Person 클래스가 있다고 가정해봅시다. 인코더는 런타임 환경에서 Person 객체를 바이너리구조로 생성하도록 스파크에게 지시합니다. DataFrame 이나 “표준" 구조적 API 를 이용한다면, Row 타입을 직렬화된 바이너리구조로 변환합니다. 도메인에 특화된 객체를 만들어 이용하려면, 스칼라의 케이스 클래스 (case class) 또는, 자바 빈 형태로 사용자 정의 데이터타입을 정의해야합니다.
- DataSet API를 이용한다면, 스파크는 데이터셋에 접근할 때마다 Row 포맷이 아닌 사용자 정의 데이터타입으로 반환합니다.
    - 이 변환 작업은 느리긴하지만, 사용자에게 더 많은 유연성을 제공합니다.
    - 사용자 정의데이터 타입을 이용하면, 성능은 나빠지게 됩니다. 이게 파이썬 udf 보다 자릿수가 달라질 정도로 훨씬 느립니다. 그 이유는 프로그래밍 언어를 전환하는 것이 사용자 정의 데이터 타입을 사용하는 것 보다 훨씬 느리기 때문입니다.


### DataSet 을 이용하는 시기
- DataSet을 이용하면, 성능이 떨어지는데, 사용할 이유가 있을까? 라는 질문에 대해 사용하는 경우에 대해 정리해봅시다.

- 사용하는 경우
- DataFrame기능만으로 수행할 연산을 표현할 수 없는 경우
    - 복잡한 비즈니스 sql 이나, DataFrame대신, 단일 함수로 인코딩해야하는 경우
- 성능 저하를 감수하더라도 타입 안정성(type safe)을 가진 데이터 타입을 사용하고 싶은 경우
- 또한,DataSet api 는 타입 안정성이 있습니다. 예를 들어두 문자열을 사용해 뺄셈 연산을 하는 것 처럼 데이터 타입이유효하지 않은 작업은 런타임이 아닌 컴파일 타임에 오류가 발생합니다.
    - 만일,정확도와 방어적 코드를 가장 중요시한다면, 성능을 희생하더라도, DataSet을 이용하는 것이 좋은 선택일 수 있습니다.
    - DataSet api 를 이용하면, 잘못된 데이터로부터 애플리케이션을 보호할수는 없지만, 보다 우아하게데이터를 제어하고 구조화할 수 있습니다.
- 단일 노드의 워크로드와 스파크 워크로드에서 전체 로우에 대한 다양한 트랜스포메이션을 재사용하려면, DataSet을 사용하는 것이 적합합니다.
    - 스칼라를 사용해본 경험이 있다면, 스파크 api는 스칼라 sequence 타입의 api 가 일부 반영돼있지만, 분산 방식으로 동작하는 것을 알 수 있을 겁니다.
        - 2015년 스칼라 창시자인 마틴 오더스키가 2015년 유럽 스파크 서밋에서 그렇게 언급했습니다.
        - 결국 DataSet을 사용하는 장점 중 하나는 로컬과 분산 환경에 재사용할 수 있는 것입니다.
            - 케이스 클래스로 구현된 데이터 타입을 이용해 모든 데이터와 트랜스포메이션을 정의하면, 재사용할 수 있습니다.
            - 또한, 올바른 클래스와 데이터 타입이 지정된 dataframe 을 로컬 디스크에 저장하면,다음 처리 과정에 이용할수 있어, 더 쉽게 데이터를 다룰 수 있습니다.
- 더 적합한 워크로드를 만들기 위해 DataFrame과 DataSet을 동시에이용해야할 수 있습니다. 하지만, 성능과 타입 안정성을 위해 반드시 희생할 수 밖에 없습니다. 이러한 방식은 대량의 DataFrame 기반의 etl 트랜스포메이션의 마지막 단계에서 이용할 수 있습니다.
    - 예를 들어 드라이버로 데이터를 수집해, 단일 노드의 라이브러리로 수집된 데이터를 처리해야하는 경우 입니다.
    - 반대로 트랜스포메이션의 첫번째 단계에서 이용할 수 있습니다. 예를들어 스파크 sql 에서 필터링 전에 로우 단위로 데이터를 파싱하는 경우 입니다.