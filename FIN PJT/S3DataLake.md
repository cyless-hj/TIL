# USE AWS S3A FILESYSTEM FOR DATALAKE
1. python 설치

2. spark 설치

3. jars 설정
- https://jhleeeme.github.io/read-aws-s3-data-on-spark/ 참조
- Hadoop 버전 확인하여 jars 파일 선택

4. spark-defaults.conf

```python
spark.driver.extraClassPath /home/big/study/db/ojdbc8.jar:/home/big/study/db/oraclepki-21.jar:/home/big/study/db/osdt_cert-21.jar:/home/big/study/db/osdt_core-21.jar:/home/big/study/db/ucp.jar
spark.jars /home/big/study/db/ojdbc8.jar,/home/big/study/db/oraclepki-21.jar,/home/big/study/db/osdt_cert-21.jar,/home/big/study/db/osdt_core-21.jar,/home/big/study/db/ucp.jar

spark.hadoop.fs.s3a.access.key= <ACCESS KEY>
spark.hadoop.fs.s3a.secret.key= <PUBLIC KEY>
spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem
```

5. spark-env.sh

```python
export PYSPARK_PYTHON=/usr/bin/python3
export PYSPARK_DRIVER_PYTHON=/usr/bin/python3
```

6. ~/.bashrc

```python
export JAVA_HOME=/home/big/java

export SPARK_HOME=/home/big/spark

export PATH=$PATH:$SPARK_HOME/bin
export PATH=$PATH:$SPARK_HOME/sbin

export PATH=$PATH:$JAVA_HOME/bin

export PATH=/home/big/.local/bin:$PATH
```

7. pyspark 설치

8. spark session

```python
def spark_session():
    conf = SparkConf()
    ## conf에 설정한 경우 key 설정 안잡아도 됌
    conf.set("spark.hadoop.fs.s3a.access.key", "ACCESS KEY")
    conf.set("spark.hadoop.fs.s3a.secret.key", "SECRET KEY")

    # S3 REGION 설정 ( V4 때문에 필요 )
    conf.set("spark.hadoop.fs.s3a.endpoint", "s3.ap-northeast-2.amazonaws.com")

    spark = SparkSession.builder \
        .config(conf=conf) \
        .appName("Learning_Spark") \
        .getOrCreate()

    # Signature V4 설정
    spark.sparkContext.setSystemProperty("com.amazonaws.services.s3.enableV4", "true")

    return spark
```