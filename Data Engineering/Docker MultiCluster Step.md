# 도커를 이용한 Hadoop container - Multi Cluster 환경 구축

**Single Cluster 환경 구축을 수정하여 진행**

1. Hadoop 설정 변경
```
cd $HADOOP_CONF_DIR
vim hadoop-env.sh
export JAVA_HOME=/big/java
export HADOOP_HOME=/big/hadoop
export HADOOP_LOG_DIR=${HADOOP_HOME}/logs
```

2. hadoop master - slaver 설정
- ref : https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html#Slaves_File

```
vim workers
# localhost 삭제
datanode1
datanode2
datanode3
```

3. 하둡 cors 처리
- ref : https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html#Configuring_the_Hadoop_Daemons
- ref : https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/HttpAuthentication.html#CORS <br>

4. core-site.xml 작성
```
vim core-site.xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://namenode:9000</value>
    </property>
    <property>
        <name>hadoop.http.cross-origin.enabled</name>
        <value>true</value>
    </property>
    <property>
            <name>hadoop.http.cross-origin.allowed-origins</name>
            <value>*</value>
    </property>
    <property>
            <name>hadoop.http.cross-origin.allowed-methods</name>
            <value>GET,POST,HEAD</value>
    </property>
    <property>
            <name>hadoop.http.cross-origin.allowed-headers</name>
            <value>X-Requested-With,Content-Type,Accept,Origin</value>
    </property>
    <property>
            <name>hadoop.http.cross-origin.max-age</name>
            <value>1800</value>
    </property>
</configuration>
```

5. hdfs-site.xml 작성
```
vim hdfs-site.xml
<configuration>
	<property>
		<name>dfs.namenode.name.dir</name>
		<value>/home/big/hadoop/namenode_dir</value>
	</property>
	<property>
		<name>dfs.datanode.data.dir</name>
		<value>/home/big/hadoop/datanode_dir</value>
	</property>
	<property>
		<name>dfs.datanode.http.address</name>
		<value>0.0.0.0:9864</value>
	</property>	
</configuration>
```

6. yarn-site.xml 작성
```
vim yarn-site.xml
<configuration>
	<property>
		<name>yarn.resourcemanager.hostname</name>
		<value>namenode</value>
	</property>
	<property>
		<name>yarn.nodemanager.log-dirs</name>
		<value>file:///hadoop/yarn/logs</value>
	</property>

# Localization : 원격의 리소스를 파일시스템으로 복사/다운로드하는 과정
# 원격의 리소스를 로컬로 가져오기.
# 로컬라이제이션 과정에서 생기는 스테이징 데이터들이 저장되는 경로
# 필요시에 , 를 사용해 여러 디렉토리를 설정할 수 있다.
# 하나의 디렉토리에 지나치게 많은 데이터가 쌓이는 것을 방지

	<property>
		<name>yarn.nodemanager.local-dirs</name>
		<value>file:///hadoop/yarn/local</value>
	</property>
</configuration>
```

7. mapred-site.xml 작성
```
vim mapred-site.xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
```

8. 이미지 commit

9. d : 백그라운드 실행
```
docker run -itd `
-h namenode `
--name namenode `
-p 9870:9870 `
-p 8088:8088 `
-p 9864:9864 `
azimemory/mcluster

docker run -itd `
-h datanode1 `
--name datanode1 `
-p 9861:9861 `
--link namenode:namenode `
azimemory/mcluster

docker run -itd `
-h datanode2 `
--name datanode2 `
-p 9862:9862 `
--link namenode:namenode `
azimemory/mcluster

docker run -itd `
-h datanode3 `
--name datanode3 `
-p 9863:9863 `
--link namenode:namenode `
azimemory/mcluster
```

10. 각 컨테이너의 ssh서버 열기
```
docker exec -it datanode1 bash
sudo service ssh start
exit

docker exec -it datanode2 bash
sudo service ssh start
exit

docker exec -it datanode3 bash
sudo service ssh start
exit

docker exec -it namenode bash
sudo service ssh star
```

11. namenode hosts 파일 작성
```
sudo vim /etc/hosts
172.29.0.2 	namenode
172.29.0.3 	datanode1
172.29.0.4 	datanode2
172.29.0.5 	datanode3
```

12. ssh 통신 확인
```
ssh datanode1
sudo service ssh starta
yes

ssh datanode2
sudo service ssh starta
yes

ssh datanode2
sudo service ssh starta
yes
```

13. 후작업
- 멀티모듈 후작업
- 모든 데이터 노드의 hdfs-site.xml에서 데이터노드의 http.address 포트를 수정
- 모든 데이터노드가 개별적인 포트를 사용해 호스트와 데이터노드 컨테이너간의 포트 통신을 가능하게끔
```
cd $HADOOP_CONF_DIR/
vim hdfs-site.xml

# datanode1
<property>
    <name>dfs.datanode.http.address</name>
    <value>0.0.0.0:9861</value>
</property>

# datanode2
<property>
    <name>dfs.datanode.http.address</name>
    <value>0.0.0.0:9862</value>
</property>

# datanode3
<property>
    <name>dfs.datanode.http.address</name>
    <value>0.0.0.0:9863</value>
</property>

#name node에서 실행
hdfs namenode -format
hdfs datanode -format
start-dfs.sh
```

14. 데이터노드의 도메인(데이터노드 컨테이너의 호스트명)이 호스트의 아이피를 가리키도록 hosts파일에서 수정
- powershell을 관리자 권한으로 실행
```
cd /windows/system32/drivers/etc
notepad hosts  # 호스트 파일 수정
127.0.0.1 datanode1
127.0.0.1 datanode2
127.0.0.1 datanode3
```