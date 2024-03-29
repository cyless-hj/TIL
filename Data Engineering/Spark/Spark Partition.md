# 파티셔닝과 셔플링

## 파티셔닝
- 데이터를 여러 클러스터 노드로 분할하는 메커니즘

### 파티션
- RDD 데이터를 나눈 것
- 스파크는 데이터를 로드하면 여러 파티션으로 분할해 클러스터 노드에 고르게 분산 저장한다.
- 이렇게 분산된 파티션이 모여서 RDD 하나를 형성한다.
- 스파크는 RDD 별로 RDD의 파티션 목록을 보관하며, 각 파티션의 데이터를 처리할 최적 위치를 추가로 저장할 수 있다.
- **파티션 개수**
    - 태스크 개수가 필요 이하로 적으면 클러스터를 충분히 활용할 수 없다.
    - 또한 각 태스크가 처리할 데이터 분량이 실행자의 메모리 리소스를 초과해 메모리 문제가 발생할 수 있다.
    - 따라서 클러스터의 코어 개수보다 서너 배 더 많은 파티션을 사용하는 것이 좋다.
    - 파티션을 조금 과다하게 늘린다고 문제가 발생하지는 않지만, 태스크가 너무 많으면 태스크 관리 작업에 병목 현상이 발생하므로 비상식적으로 큰 값을 설정하면 안된다.

### Spark Partitioner
- RDD의 데이터 파티셔닝은 RDD의 각 요소에 파티션 번호를 할당하는 Partitioner 객체가 수행
- HashPartitioner, RangePartitioner, 사용자 정의 Partitioner

#### HashPartitioner
- Spark의 기본 Partitioner
- 각 요소의 자바 해시 코드(Pair RDD는 키의 해시 코드)를 단순한 mod 공식(partitionIndex = hashCode % numberOfPartitions)에 대입해 파티션 번호 계산
- 각 요소의 파티션 번호를 거의 무작위로 결정하기 때문에 모든 파티션을 정확하게 같은 크기로 분할할 가능성이 낮다.
- **하지만** 대규모 데이터셋을 상대적으로 적은 수의 파티션으로 나누면 대체로 데이터를 고르게 분산시킬 수 있다.
- HashPartitioner를 사용할 경우 데이터 파티션의 기본 개수는 스파크의 spark.default.parallelism 환경 매개변수 값으로 결정
    - 이 매개변수를 지정하지 않으면 스파크는 클러스터의 코어 개수를 대신 사용

#### RangePartitioner
- 정렬된 RDD의 데이터를 거의 같은 범위 간격으로 분할할 수 있다.
- 대상 RDD에서 샘플링한 데이터를 기반으로 범위 경계를 결정
- 하지만 직접 사용할 일은 많지 않다.

#### Pair RDD와 사용자 정의 Partitioner
- 파티션(또는 파티션을 처리하는 태스크)의 데이터를 특정 기준에 따라 정확하게 배치해야 할 경우 **사용자 정의 Partitioner**로 Pair RDD 분할
    - ex) 각 태스크가 특정 키-값 쌍 데이터만 처리해야 할 때 사용자 정의 Partitioner를 쓸 수 있다.
- 사용자 정의 Partitioner
    - Pair RDD에만 쓸 수 있다.
    - Pair RDD의 변환 연산자를 호출할 때 사용자 정의 Partitioner를 인수로 전달
    - Pair RDD를 호출할 때 Partitioner를 따로 지정하지 않으면 스파크는 부모 RDD에 지정된 파티션 개수 중 가장 큰 수를 사용한다.
    - Partitioner를 정의한 부모 RDD가 없다면 spark.default.parallellism 매개변수에 지정된 파티션 개수로 HashPartitioner를 사용
    - 기본 Partitioner를 그대로 사용하면서 임의의 알고리즘으로 키의 해시 코드만 바꾸어도 Pair RDD 데이터의 파티션 배치를 변경할 수 있다.
        - 일부 사례에서는 이 방법이 오히려 구현하기 더 쉽고, 부주의한 셔플링을 피할 수 있어 성능도 향상할 수 있다.

### 불필요한 셔플링

#### 셔플링
- 파티션 간의 물리적인 데이터 이동
- 새로운 RDD를 만들기 위해 여러 파티션의 데이터를 합칠 때 발생

#### Map task - Shuffle - Reduce task
- Map : key-value 형태로 데이터를 만듬
- Reduce : key를 기준으로 데이터를 정렬

#### 셔플링 발생 조건
##### Partitioner를 명시적으로 변경하는 경우
- 사용자 정의 Partitioner를 쓰면 반드시 셔플링 발생
- 이전 HashPartitioner와 다른 HashPartitioner를 사용해도 셔플링 발생
    - HashPartitioner 객체가 다르더라도 동일한 파티션 개수를 지정했다면 같다고 간주
    - 이전에 사용한 HashPartitioner와 **파티션 개수가 다른 HashPartitioner**를 사용하면 셔플링 발생

##### Partitioner를 제거하는 경우
- map과 flatMap은 RDD의 Partitioner를 제거
- 이 자체로는 셔플링이 발생하지 않지만 RDD에 다른 변환 연산자(aggregateByKey나 foldByKey) 사용하면 기본 Partitioner를 사용했더라도 셔플링 발생