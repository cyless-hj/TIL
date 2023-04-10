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

## Linux
- 명령어가 보여주는 결과
- 권한 설정을 어떻게 하고 권한은 어떤 형식으로 보여지는가

## Python
- 파이썬은 인터프리터 언어이다.
- 인터프리터 언어 : 소스 코드를 컴파일하지 않고 인터프리터로 소스코드를 한 줄씩 번역하면서 실행하는 방식으로 동작하는 언어
    - 빌드 과정 없이 바로 실행이 가능하다. → 별도의 실행 파일이 없다.
    - 컴파일과정 없이 바로 실행하기 때문에 수정, 디버깅에 유리하다. 즉 개발속도에 유리하다.
    - 각 플랫폼에 지원하는 인터프리터만 있다면 실행 가능하기 때문에 플랫폼에 독립적이다.

- 컴파일러와 인터프리터 비교 정리
    - 컴파일러는 소스코드 전체를 CPU가 읽을 수 있는 기계어로 변환한다. 인터프리터는 소스코드 각 행을 기계어로 번역한다.
    - 그래서 오류가 나면 컴파일러는 컴파일 하는 도중에 오류가 나고, 인터프리터는 분석 도중 어느 행에 오류가 발생하면 그것을 알려주고 그 이후의 분석을 멈춘다.

    - 오류 발생 시 인터프리터 언어는 수정 후 바로 사용 가능
    - 컴파일러 언어는 수정 후 재 컴파일 후 실행 가능

    - 속도는 컴파일 언어가 컴파일 완료 후 실행하기 때문에 한줄 한줄 해석해 사용하는 인터프리터 언어보다 빠르다.

## 비동기 함수
- 동기 함수 : 함수 요청 후 함수 완료까지 대기
- 비동기 함수 : 호출한 함수의 실행이 다 끝나지 않았어도 호출한 함수에게 return 하고, 백그라운드에서 실행, 작업 완료 후 통보
    - 동기 함수와 다르게 작업 완료를 보장해주지 않는다.
- **비동기 처리를 사용하는 이유**
    - CPU의 유휴 시간을 줄여 프로그램의 성능을 높이는 것

- 파이썬의 비동기 함수
    - 함수 정의
        ```python
        async def
        ```
        - async def 를 이용한 함수를 **코루틴**이라 한다.
    - asyncio 라이브러리
        - 동기 함수를 비동기 함수로 사용할 수 있다.
        ```python
        import time
        import asyncio


        async def good_night():
            await asyncio.sleep(1)
            print('잘자요')


        async def main():
            await asyncio.gather(
                good_night(),
                good_night()

            )
        print(f"start : {time.strftime('%X')}")
        asyncio.run(main())
        print(f"end : {time.strftime('%X')}")
        ```
### await
- 특정 객체가 끝날 때까지 기다리는 역할을 한다.
- await 를 사용하면 비동기 작업이 완료되었다는 통보가 올 때까지 대기하지만,
- event loop 를 확인하여 event loop 내 task 가 존재한다면 그 일을 처리한다.
    - 자, 그렇게 된다면 우리는 event loop 에 두 개의 good_night 함수를 넣어
    - 첫번째 good_night 함수의 sleep 만료 통보를 기다리는 동안,
    - 두번째 good_night 함수를 처리하면 되는 것이다.
- asyncio.gather() 를 이용하여 await 키워드가 붙은 good_night() 을 event loop 에 등록한다.
- 이후 asyncio.run() 함수를 통해 비동기 함수를 호출하면 된다.

## NoSQL 관계 데이터
- NoSQL도 관계 데이터를 저장할 수 있다.
- RDB처럼 여러 테이블에 나누어 담지 않고, 관련 데이터를 동일한 **컬렉션**에 넣는다.

## RDB VS NoSQL 많은 데이터를 담는데 적합한 것은?
- RDB는 수평적 확장이 어렵고 수직적 확장만 가능(데이터 처리량에 관련된 한계 존재)
- NoSQL은 수직적 확장, 수평적 확장 모두 가능
- NoSQL이 더 많은 데이터를 담는데 적합하다.