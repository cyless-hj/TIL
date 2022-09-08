# Docker-compose
- docker compose는 이미 생성된 이미지를 기반으로 다수의 컨테이너를 일괄적으로 운용해야할 때 사용한다.

## dockerfile vs docker-compose
- dockerfile은 이미지를 생성하는 용도이고, docker compose는 여러 컨테이너를 
수월하게 다루기 위해 사용한다.

## docker-compose 명령어
- docker-compose up : 컨테이너를 생성하고 시작
- docker-compose stop : 컨테이너를 정지
- docker-compose start : 정지된 컨테이너를 시작
- docker-compose restart : 재시작
- docker-compose kill : 컨테이너 강제 정지
- docker-compose rm : 컨테이너 삭제

## docker-compose 예시
```
services:
  namenode:
    container_name: namenode
    hostname: namenode
    image: jhjzmdk/mcluster
    ports:
      - "9870:9870"
      - "8088:8088"
      - "9864:9864"
    command: sh -c "sudo service ssh start && sleep infinity"
  
  datanode1:
    container_name: datanode1
    hostname: datanode1
    image: jhjzmdk/mcluster
    ports:
      - "9861:9861"
    links:
      - namenode
    command: sh -c "sudo service ssh start && sleep infinity"

  datanode2:
    container_name: datanode2
    hostname: datanode2
    image: jhjzmdk/mcluster
    ports:
      - "9862:9862"
    links:
      - namenode
    command: sh -c "sudo service ssh start && sleep infinity"

  datanode3:
    container_name: datanode3
    hostname: datanode3
    image: jhjzmdk/mcluster
    ports:
      - "9863:9863"
    links:
      - namenode
    command: sh -c "sudo service ssh start && sleep infinity"
```

## sleep infinity를 사용하는 이유
- shell은 코드 진행이 끝나면 대기상태가 풀린다.
- 우리의 입력에 대해 대기할 필요가 있어 sleep infinity로 코드 진행 상태가 끝나지 않도록 해주는 것이다.