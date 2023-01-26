# List to Study

## Hadoop이란
- Hadoop의 개념
    - namenode와 datanode의 정의와 동작 원리
    - mapReduce 의 동작원리
        - map과 reduce로 나누어 설명 가능할 것
    - block 형태의 데이터 저장
        - 이로인한 장점과 단점
- Hadoop 튜닝
- Hadoop 버전에 따른 차이와 프로젝트에서 해당 버전을 사용한 이유

## Spark란
- Spark의 개념, 역할
- Spark 동작 원리
    - context 등
- Spark 튜닝
- Spark 세션을 많이 사용하면 안된다.
    - 세션 사용 수를 줄이는 방법은?
    - 왜 세션을 많이 사용하면 안되는가?
- RDD, Dataframe, DataSet을 사용할 수 있다.
    - 프로젝트에서는 DataFrame을 사용했다.
    - DataSet이 최근에 나왔다.
    - DataSet을 사용하지 않은 이유는?
        - Python 기반인 PySpark를 사용했고 PySpark에서는 이를 지원하지 않는다.

## Kafka
- Kafka의 속도를 높이기 위한 방법
    - 컨슈머 수를 늘리면 속도가 빨라질까?

## Airflow
- 배치가 짧은시간 안에 돌아야만 할 수 있다. 성능을 올리려면 병렬 처리 수를 줄이는 것이 아닌 방법이 뭐가 있을까?
    - Docker환경의 CPU와 RAM 할당을 늘리는 방법은 사용해보았다.
    - 다른 방법이 또 있을까?

## Kubernetes
- Kubernetes란
- 사용해볼 것

## Java
- Exception이 잘 발생한다.
- 이에 대한 경우를 살펴보고 해결방안은 무엇이 있을지 알아보자.