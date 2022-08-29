# Docker
- 리눅스의 응용 프로그램들을 컨테이너로 패키징 해주는 컨테이너화 기술

## Docker Server
- 컨테이너를 생성, 실행, 이미지를 관리하는 주체

## Docker Client
- Docker Server에게 컨테이너 생성, 실행 이미지 관리를 지시할 수 있는 API를 사용할 수 있도록 Interface를 제공해줌

## Docker : 명령어
- pull : docker pull <저장소명/이미지명:태그>
- push : docker push <(push 할)저장소명/이미지명:태그> <(dockhub의)저장소명/이미지명:태그>
- commit : docker commit <컨테이너이름 or 컨테이너id > <저장할 이미지명> <br>

- 실행 : *이미지로부터 컨테이너를 생성
    - docker run -d --name <컨테이너 이름> -p <로컬포트:도커포트> <이미지이름 or 이미지id>
    - -d : 백그라운드로 실행
- 도커 실행 후 쉘로 돌아오기 : exit
- 컨테이너 시작 : 중지된 컨테이너를 시작 docker start <컨테이너이름 or 컨테이너id >
- 컨테이너 재부팅 : docker restart <컨테이너이름 or 컨테이너id>
- 컨테이너 중지 : docker stop <컨테이너이름 or 컨테이너id >
- 실행중인 컨테이너로 접근 하기 : docker exec -it <container_id> bash / 돌아오기 : ctl - z
- 실행 중인 컨테이너 조회 : docker ps / 중지된 컨테이너도 모두 조회 : docker ps –a
- 컨테이너 중지 : docker stop <컨테이너이름 or 컨테이너id >
- 컨테이너 삭제 : docker rm <컨테이너이름 or 컨테이너id > <br>

- 이미지 확인 : docker images
- 이미지 삭제 : docker rmi <이미지명 or 이미지id >
- 이미지 이름 변경 : docker image tag <기존 이미지명>:<기존 태그명> <새 이미지명>:<새 태그명>
