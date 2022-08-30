# 도커를 이용한 Hadoop container 설정

1. 우분투 기반 컨테이너 실행
```
docker run -it --name de_base ubuntu:20.04
```
- -it : 컨테이너의 터미널에 접근
-  --name : 컨테이너 이름

2. 패키지 관리자 업데이트
```
apt update -y
apt upgrade -y
apt install wget vim unzip sudo -y
```
- -y : 업데이트 진행여부를 물어볼 때 y를 자동으로 입력 <br>

- wget : 웹에서 파일을 다운로드
- vim : 텍스트 에디터
- unzip : 알집
- sudo : sudo 명령어를 쓰기위해 설치


3. 사용자 생성
```
useradd -m big
```
- -m : 사용자를 생성하면서 홈디렉터리도 같이 생성 <br>

- 사용자@호스트:위치[#,$]
	- 사용자 : 사용자
	- 호스트 : 네트워크에서 해당 컴퓨터를 식별하기 위한 이름
	- (#) : super user
	- $ : 일반사용자 <br>

## 사용자 목록 확인
```
cat /etc/passwd
```
- big: x :1000:1000::/home/big:/bin/sh
    - big : 사용자명
    - x : 암호화된 password
    - 1000 : userId
    - 1000 : 그룹번호
    - 추가정보
    - /home/big : 홈디랙터리
    - /bin/sh : login 시 사용할 쉘

4. big 사용자의 쉘 설정을 변경
- big: x :1000:1000::/home/big:/bin/sh => big: x :1000:1000::/home/big:/bin/bash
- /etc/passwd 파일을 수정
```
vim /etc/passwd
```
- i를 사용해 입력모드로 진입
- 수정
- esc + wq (저장 및 나가기) <br>

5. 사용자 상세 정보
```
vim /etc/shadow
```

- root 권한이 필요하다
    - root권한 빌려오기
    - sudo 명령어

6. 사용자 비밀번호 설정
```
passwd root
passwd big
```

7. sudoers 파일 수정
```
vim /etc/sudoers
big     ALL=(ALL:ALL) ALL
```

8. 도커허브에 push
- 도커 로그인을 하지 않았다면 docker login 명령어를 통해 로그인 진행
```
docker commit <이미지이름> <도커허브유저명/컨테이너이름:버전>
docker push <도커허브유저명/컨테이너이름:버전>
```

9. java download <br>
**big 계정에서 진행**
```
wget https://corretto.aws/downloads/latest/amazon-corretto-11-x64-linux-jdk.tar.gz
```

10. 자바파일 압축 해제
```
tar xvzf amazon-corretto-11-x64-linux-jdk.tar.gz
```

11. 자바 심볼릭링크 설정
```
ln -s amazon-corretto-11.0.16.9.1-linux-x64/ java
```

12. vim ~/.bashrc 파일에 환경변수 등록
```
vim ~/.bashrc 
export JAVA_HOME=/home/big/java
export PATH=$PATH:$JAVA_HOME/bin
```
- 위 export 추가
- 저장
    - :wq!
- ~/.bashrc 실행
```
source ~/.bashrc
```

13. ssh 설치 및 키 등록
```
sudo apt-get install ssh
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

14. 하둡설치
```
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz
tar -xvzf hadoop-3.3.4.tar.gz 
```

15. hadoop-env.sh 파일 수정
```
export JAVA_HOME=/home/big/java
```
- 저장

## hadoop 문서보기
```
cd /home/big/hadoop/bin/
./hadoop
```

16. 홈디랙토리에서 hadoop directory 생성
```
cd 
mkdir hadoop/temp
mkdir hadoop/pids
mkdir hadoop/namenode_dir
mkdir hadoop/secondary_dir
mkdir hadoop/datanode_dir
mkdir hadoop/logs
```

17. yarn directory 생성
```
mkdir -p hadoop/yarn/logs
mkdir -p hadoop/yarn/local
```

18. hadoop 환경변수 등록
```
vim ~/.bashrc  
export JAVA_HOME=/home/big/java
export PATH=$PATH:$JAVA_HOME/bin
export HADOOP_HOME=/home/big/hadoop
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
```

19. 이미지 commit
```
docker commit <컨테이너명> <이미지명>
docker push <이미지명>
docker push azimemory/hadoop_base:1.0
```

20. vim colorscheme 설정
- 홈디렉토리 아래에서
```
vim .vimrc
colorscheme pablo
```
- 저장

21. hadoop Pseudo-Distributed Operation 설정
- ref : https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html#Pseudo-Distributed_Operation
```
cd $HADOOP_CONF_DIR
```

```
vim hadoop-env.sh
export JAVA_HOME=/home/big/java
```

22. core-site.xml 작성
```
vim core-site.xml
<configuration>
	<property>
		<name>fs.defaultFS</name>
		<value>hdfs://localhost:9000</value>
	</property>
</configuration>
```

23. hdfs-site.xml 작성
```
vim hdfs-site.xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>

    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/home/big/hadoop/namenode_dir</value>
    </property>

    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/home/big/hadoop/datanode_dir</value>
    </property>
</configuration>
```

24. mapred-site.xml 작성
```
vim mapred-site.xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
```

25. hadoop user
```
export HDFS_NAMENODE_USER=big
export HDFS_DATANODE_USER=big
export HDFS_SECONDARYNAMENODE_USER=big
export YARN_RESOURCEMANAGER_USER=big
export YARN_NODEMANAGER_USER=big

hdfs namenode -format
hdfs datanode -format

start-dfs.sh
```

26. namenode, datanode, secondary namenode 가 올라간 것을 확인
```
jps
```

27. docker commit ...

28. 기존의 컨테이너 stop, 포트바인딩을 하여 새로운 컨테이너를 생성
```
docker run -it
--name scluster
-h localhost		#호스트명을 지정
-p 18080:18080		#<호스트포트>:<컨테이너포트> spark web ui
-p 9870:9870		#namenode
-p 8081:8081		#jupyter notebook
-p 9864:9864		#datanode
#####################
-p 8088:8088		#yarn resourceManager
####################
azimemory/singlenode:1.0

docker run -it `
--name scluster `
-h localhost `
-p 18080:18080 `
-p 9870:9870 `
-p 9864:9864 `
-p 8081:8081 `
azimemory/singlenode:1.0

docker run -it --name scluster -h localhost -p 18080:18080 -p 9870:9870 -p 8081:8081 azimemory/singlenode:1.0
```

29. hdfs의 / 에 권한을 777로 설정
```
su big
sudo service ssh start
start-dfs.sh
hdfs dfs -chmod 777 /
```

