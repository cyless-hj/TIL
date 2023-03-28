# DataFrame
- Column 이름과 Type이 지정된 테이블 형식의 분산 정형 데이터를 손쉽게 다룰 수 있는 상위 레벨 인터페이스 제공
- 플러그인으로 확장 가능한 데이터 소스, 규칙, 데이터 타입 등을 바탕으로 리소스 사용량을 실시간으로 최적화하는 스파크 카탈리스트 엔진 사용
- SQL 및 도메인 특화 언어(DSL)로, 작성된 표현식을 최적화된 하위 레벨 RDD 연산으로 변환
- RDD 기반으로 지연 실행, 불변성
    - 직접 데이터를 변경할 수 없다
- 생성 방법
    1. 기존 RDD를 변환
    2. SQL 쿼리를 실행
    3. 외부 데이터에서 로드

## RDD에서 DataFrame 생성
- 생성 방법
    1. ROW의 데이터를 튜플 형태로 저장한 RDD를 사용하는 방법
    ```python
    def get_spark_session():
    findspark.init()
    return SparkSession.builder.getOrCreate()
    
    rd = [
    Row(name='정현진', age=26, birth=date(1997,8,30)),
    Row(name='하명도', age=21, birth=date(2001,9,6)),
    Row(name='이상엽', age=22, birth=date(2000,10,8))
    ]
    rdd = get_spark_session().sparkContext.parallelize(rd)
    df_rd = rdd.toDF()
    df_rd.show()
    ```

    2. 케이스 클래스를 사용하는 방법
    3. 스키마를 명시적으로 지정하는 방법
    ```python
    df = spark.createDataFrame([
    Row(name='정현진', age=26, birth=date(1997,8,30)),
    Row(name='하명도', age=21, birth=date(2001,9,6)),
    Row(name='이상엽', age=22, birth=date(2000,10,8))
    ])

    df.show()
    ```

### schema를 명시하여 DataFrame 생성
- 튜플에 데이터를 저장하고 스키마를 직접 지정
```python
df = spark.createDataFrame([
    ('김경민', 17, date(2005, 10, 11)),
    ('김도은', 18, date(2004, 12, 25)),
    ('김민석', 11, date(2011, 1, 10))
], schema='name string, age int, birth date')

df.show()
df.printSchema()
```

### StructType 객체를 사용해 Schema 지정
```python
schema = StructType([
    StructField("name", StringType(), False),
    StructField("age", IntegerType(), False),
    StructField("birth", DateType(), False),
    StructField("is_pass", BooleanType(), False)
])

df = spark.createDataFrame([
    ('손지수', 22, date(2011, 6, 8), True),
    ('유승종', 21, date(2009, 8, 28), True),
    ('윤병우', 23, date(2022, 3, 3), True)
])

df.show()
df.printSchema()
```

### 중첩스키마적용
```python
data = [
    ('이서정', 21, date(2000, 11, 11), ('010', '1111', '2222')),
    ('이선희', 25, date(1999, 11, 11), ('010', '2222', '3333')),
    ('정주연', 23, date(2244, 6, 23), ('010', '3333', '4444'))
]

schema = StructType([
    StructField("name", StringType(), False),
    StructField("age", IntegerType(), False),
    StructField("birth", DateType(), False),
    StructField("phone", StructType([
        StructField("phone1", StringType(), False),
        StructField("phone2", StringType(), False),
        StructField("phone3", StringType(), False)
    ]), False, metadata = {'desc':'user phone number'})
])

df = spark.createDataFrame(data = data, schema = schema)
df.show()
df.printSchema()

schema_of_json = df.schema.json
print(schema_of_json)
```

### Pandas DataFrame으로 생성
```python
pandas_df = pd.DataFrame({
    'name':['정현진', '한병현', '홍효정'],
    'age':[20, 21, 22],
    'birth':[date(2000, 1, 1), date(2001, 2, 2), date(2005, 5, 5)]
})

pandas_df
df = spark.createDataFrame(pandas_df)
df.show()
```

### DataFrame -> Pandas
```python
pandas_df = df.toPandas()
```

### DataFrame -> pyspark.pandas
```python
pandas_df = df.to_pandas_on_spark()
```

### 외부파일을 사용해 DataFrame 생성
```python
class_df = spark.read.csv('/dataframe/a_class_info.csv', header = True)
```

### 외부파일을 사용해 DataFrame 생성
```python
class_df = spark.read.csv('/dataframe/a_class_info.csv', header = True)
```

## withColumn
```python
df = df.withColumn('성별', lit(''))
df.show(3)

# 기본값 지정, withColumn 사용 시 기존의 컬럼과 컬럼명이 같으면 덮어쓴다
df = df.withColumn('성별', lit('F'))
df.show(3)

# 조건에 따라 다른 컬럼 값을 가지도록 컬럼을 추가
# when - otherwise
temp = df.withColumn('성별', when(df.age < 23, '여성')
                            .when(df.age == 23, 'F')
                            .otherwise('Female'))

temp.show(3)
```

### column 내용  변경
```python
df4 = df4.withColumn('성별', lit(''))
df4.show(3)

# 기본값 지정, withColumn 사용 시 기존의 컬럼과 컬럼명이 같으면 덮어쓴다
df4 = df4.withColumn('성별', lit('F'))
df4.show(3)
```

### column 이름 변경
```python
temp = temp.withColumnRenamed('성별', 'gender')
temp.show()
```

### column  삭제
```python
temp = temp.drop('gender')
temp.show()
```

## select()
```python
class_df = spark.read.csv('/dataframe/a_class_info.csv', header=True)

# str
df_spark = class_df.select('school', 'loc')
df_spark.show(3)

# *
df_spark = class_df.select('*')
df_spark.show(3)

# list
df_spark = class_df.select(['class_cd', 'school'])
df_spark.show(3)
```

### Column
```python
df_spark = class_df.select(col('school'))
df_spark.show(3)

df_spark = class_df.select(class_df.school)
df_spark.show(3)

df_spark = class_df.select(class_df.colRegex("`^school.*`"))
df_spark.show(3)

df_spark = class_df.select(lit('school'))
df_spark.show(3)
```

#### Column 메서드
```python
school = class_df.school
class_cd = class_df.class_cd
std_cnt = class_df.class_std_cnt

std_cnt.asc()
class_df.select(school, class_cd, std_cnt).sort(std_cnt.asc()).show(100)
class_df.select(school, class_cd, std_cnt).sort(std_cnt.desc()).show(100)
```

### select 연습
```python
from pyspark.sql import functions as F
cdf = class_df

# 모든 row의 class_cd, school, loc, school_type, teaching_type을 출력하시오.
# school_type의 컬럼명은 '공립/사립여부' 로 표시합니다.
# hint : alias()
cdf.select('class_cd', 'school', 'loc', class_df.school_type.alias('공립/사립여부'), 'teaching_type').show()

# class_cd, school, scale 을 출력하시오.
# scale 컬럼은 반의 인원수가 15명 미만이면 small, 15명 이상 25명 미만이면 middle, 25명 이상이면 big 값을 가집니다.
# hint : when()
class_df.printSchema()
class_df.select('class_cd', 'school', (when(class_df.class_std_cnt < 15, 'small') 
                                            .when((class_df.class_std_cnt >= 15) & (class_df.class_std_cnt < 25), 'middle')
                                            .otherwise('big')).alias('scale')).show(3)

# class_cd, school, class_std_cnt를 출력하시오
# class_std_cnt 컬럼의 값들은 string타입으로 형변환합니다.
# hint : cast()
class_df.select('class_cd', 'school', class_df.class_std_cnt.cast('string')).printSchema()
```

### sql
```python
# sql을 사용해 같은 결과를 받아보기

# dataFrame을 테이블로 등록
class_df.createOrReplaceTempView('class')

# 모든 row의 class_cd, school, loc, school_type, teaching_type을 출력하시오.
# school_type의 컬럼명은 '공립/사립여부' 로 표시합니다.
# alias 지정시 ``(백틱) 사용
spark.sql('''
    select class_cd, school, loc, school_type as `공립/사립여부`, teaching_type from class
''').show(3)


# class_cd, school, scale 을 출력하시오.
# scale 컬럼은 반의 인원수가 15명 미만이면 small, 15명 이상 25명 미만이면 middle, 25명 이상이면 big 값을 가집니다.
spark.sql('''
    select class_cd, school,
        case when class_std_cnt < 15 then 'small'
               when class_std_cnt >= 15 and class_std_cnt < 25 then 'middle'
               else 'big'
        end as scale
    from class
''').show(3)


# class_cd, school, class_std_cnt를 출력하시오
# class_std_cnt 컬럼의 값들은 string타입으로 형변환합니다.
# spark built-in-fnc 의 cast()
spark.sql('''
    select class_cd, school, cast(class_std_cnt as string) from class
''').printSchema()
```

## where(), filter()
```python
class_df.printSchema()

print('공립이면서 교육방식이 전문인 데이터를 출력하시오.')
class_df.select('*') \
            .where((class_df.school_type == 'Public') & (class_df.teaching_type == 'Experimental')) \
.show(3)

print('사립이면서 교육방식이 표준 데이터를 출력하시오.')
class_df.select('*') \
            .where((class_df.school_type == 'Non-public') & (class_df.teaching_type == 'Standard')) \
.show(3)

print('학교 이름이 V로 시작하는 데이터를 출력하시오.')
class_df.select('*') \
            .where(class_df.school.like ('V%')) \
.show(3)

class_df.select('*') \
            .where(class_df.school.startswith('V')) \
.show(3)

print('학교 이름이 M로 끝하는 데이터를 출력하시오.')
class_df.select('*') \
            .where(class_df.school.endswith('M')) \
.show(3)

print('학교 이름에 NKY가 들어가는 데이터를 출력하시오.')
class_df.select('*') \
            .where(class_df.school.contains('NKY')) \
.show(3)

print('반의 학생 수가 15명 이상 24명 이하인 데이터를 출력하시오.')
class_df.select('*') \
            .where(class_df.class_std_cnt.between (15, 24)) \
.show(3)

print('학교 이름이 입력되지 않은 데이터들을 출력하시오')
class_df.select('*') \
            .where(class_df.school.isNull()) \
.show(3)
```

### sql
```python
class_df.printSchema()

print('공립이면서 교육방식이 전문인 데이터를 출력하시오.')
spark.sql('''
    select * from class where school_type = 'Public' and teaching_type = 'Experimental'
''').show(3)

print('사립이면서 교육방식이 표준 데이터를 출력하시오.')
spark.sql('''
    select * from class where school_type = 'Non-public' and teaching_type = 'Standard'
''').show(5)

print('학교 이름이 V로 시작하는 데이터를 출력하시오.')
spark.sql('''
    select * from class where school like 'V%'
''').show(3)

print('학교 이름이 M로 끝하는 데이터를 출력하시오.')
spark.sql('''
    select * from class where school like '%M'
''').show(3)

print('학교 이름에 NKY가 들어가는 데이터를 출력하시오.')
spark.sql('''
    select * from class where school like '%NKY%'
''').show(3)

print('반의 학생 수가 15명 이상 24명 이하인 데이터를 출력하시오.')
spark.sql('''
    select * from class where class_std_cnt between 15 and 24
''').show(3)

print('학교 이름이 입력되지 않은 데이터들을 출력하시오')
spark.sql('''
    select * from class where school is null
''').show(3)
```

## 윈도 함수
- 집계 함수와 유사하지만, 로우들을 단일 결과로만 그루핑하지 않는다는 점이 다르다.
- 움직이는 그룹, **프레임**을 정의할 수 있다.
    - 윈도 함수가 현재 처리하는 로우와 관련된 다른 로우 집합으로 정의하며, 이 집합을 현재 로우 계산에 활용할 수 있다.
    - ex) 이동 평균, 누적 합 등

## 결측값 다루기
### drop()
- df.na.drop() -> 1개 컬럼 이상 null이나 NaN 값 가진 모든 Row를 제외
- df.na.drop('any') -> 1개 컬럼 이상 null이나 NaN 값 가진 모든 Row를 제외
- df.na.drop('all') -> 1개 컬럼이라도 null이나 NaN 값 가진다면 Row 제외

### fill()
- df.na.fill('0')
- null이나 NaN 값을 채운다.

### replace()
- df.na.replace()
- 값 치환
