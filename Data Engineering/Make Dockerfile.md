# dockerfile
- dockerfile은 docker image를 구성하는 용도로 사용된다.

## dockerfile vs docker-compose
- dockerfile은 이미지를 생성하는 용도이고, docker compose는 여러 컨테이너를 
수월하게 다루기 위해 사용한다.

## dockerfile 작성 문법
- FROM : Docker Base Image (기반이 되는 이미지, <이미지 이름>:<태그> 형식으로 설정)
- SHELL : Default Shell 지정
- RUN : Shell Script 또는 명령을 실행
- USER : 명령 실행할 사용자 권한 지정
- WORKDIR : "RUN", "CMD", "ENTRYPOINT" 명령이 실행될 작업 디렉터리<br><br>

## dockerfile 작성 예시
```
FROM ubuntu:20.04
SHELL ["/bin/bash", "-c"]
RUN apt update -y
RUN apt upgrade -y

RUN apt install wget vim unzip sudo -y

RUN useradd -m big
RUN echo 'big    ALL=NOPASSWD: ALL' >> /etc/sudoers

USER big
WORKDIR /home/big
RUN wget https://corretto.aws/downloads/latest/amazon-corretto-11-x64-linux-jdk.tar.gz
RUN tar xvzf amazon-corretto-11-x64-linux-jdk.tar.gz
RUN rm amazon-corretto-11-x64-linux-jdk.tar.gz

# java 심볼릭링크 설정
RUN ln -s $(ls |grep 'amazon-corretto-11*') java

RUN sudo apt-get install ssh -y
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# 하둡설치
RUN wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz
RUN tar -xvzf hadoop-3.3.4.tar.gz 
RUN rm hadoop-3.3.4.tar.gz 
RUN ln -s $(ls |grep 'hadoop-3*') hadoop
RUN echo 'export JAVA_HOME=/home/big/java' >> /home/big/hadoop/etc/hadoop/hadoop-env.sh

# 하둡 디랙토리 설치
WORKDIR /home/big/hadoop
RUN mkdir temp pids namenode_dir secondary_dir datanode_dir logs
RUN mkdir -p yarn/logs yarn/local

RUN echo 'export JAVA_HOME=/home/big/java' >> ~/.bashrc
RUN echo 'export PATH=$PATH:$JAVA_HOME/bin' >> ~/.bashrc
RUN echo 'export HADOOP_HOME=/home/big/hadoop' >> ~/.bashrc
RUN echo 'export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop' >> ~/.bashrc
RUN echo 'export PATH=$PATH:$HADOOP_HOME/bin' >> ~/.bashrc
RUN echo 'export PATH=$PATH:$HADOOP_HOME/sbin' >> ~/.bashrc

RUN echo 'colorscheme pablo' >> ~/.vimrc
```

## 작성 후
- dockerfile로 생성한 컨테이너를 이용할 경우 dockerfile에서 잡아주지 못한 상세 설정들을 변경할 필요가 있다.