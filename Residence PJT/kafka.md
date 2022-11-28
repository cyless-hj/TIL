# 카프카 - Data PipeLine - Django 연동

## 카프카 설치 : https://kafka.apache.org/quickstart
    - cd ~
    - ls
    - wget https://dlcdn.apache.org/kafka/3.3.1/kafka_2.13-3.3.1.tgz
    - tar -xzf kafka_2.13-3.3.1.tgz
    - cd kafka_2.13-3.3.1

## zokeeper, kafka 순서로 올리기

### Start the ZooKeeper service
- bin/zookeeper-server-start.sh config/zookeeper.properties

### 새 powershell
### Start the Kafka broker service
- bin/kafka-server-start.sh config/server.properties

### 새 powershell
- vim config/kraft/server.properties # 카프카 설정 파일
- log.retention.hours = 시간 변경

### CREATE A TOPIC TO STORE YOUR EVENTS
- bin/kafka-topics.sh --create --topic project-log --bootstrap-server localhost:9092

### 토픽확인
- bin/kafka-topics.sh --bootstrap-server=localhost:9092 --list

### 모듈 설치
- pip install django-session-timeout

    - session : 사용자가 얼마나 체류했는지 등등 을 하기 위한 세션, 일정시간 이후 혹은 브라우져를 껏을 때 로그아웃이 되도록 타임아웃 건다

- pip install kafka-python

### middleware.py추가

### settings.py
MIDDLEWARE_APPS [
'django_session_timeout.middleware.SessionTimeoutMiddleware',
middleware.py
]

### main.py
- writestream에 s3 버킷 설정

### 웹 서버 올리기

### 새 powershell
- D_corona에서 python3 main.py
