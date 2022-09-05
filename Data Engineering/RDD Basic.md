# Spark 데이터 종류
- RDD : Low-level API에 해당 하는 데이터, 스파크에서 동작하는 모든 데이터는 결국 RDD형태로 연산된다  
- DataFrame : 열과 행으로 이루어진 테이블 형태의 데이터
- DataSet : 한가지 타입의 값만 저장할 수 있는 DataFrame. PySpark에서는 사용하지 않음

## RDD 

### Resillient Distributed Data
- Resillient : 회복력 있는  
- Distributed : 분산  
- Data : 데이터  
    * Resilient : 장애가 발생할 경우 자동으로 데이터를 복구
    * Distributed : 데이터를 읽고 쓸 때 데이터를 파티셔닝 하여 병렬로 읽고 쓴다. 직렬로 모두 읽을 때 보다 속도가 빠르다
 
 
### RDD의 특징
- Read Only : 변경불가능 객체
- Lazy Evaluation : 늦은 수행

### RDD 파티셔닝
- 커다란 RDD를 처음 부터 끝까지 직렬로 읽고 쓰면 시간이 오래 걸린다.
- RDD를 작은 부분(Partition) 으로 쪼개 각 Patition 을 병렬로 읽고 써 실행속도를 향상시킬 수 있다.
- Patition을 나눠줄때는 스파크 클러스터 환경의 cpu core 숫자에 맞춰주는 것이 속도 측면에서 유리하다.

### RDD - 생성
```python
# RDD로 만들 데이터, 파티셔닝 수
distData = sc.parallelize(data, 5)

# RDD 확인

# collect : RDD에 있는 데이터를 list로 반환하는 함수
distData.collect()

# RDD 파티셔닝 개수 확인
distData.getNumPartitions()

# RDD로 만들 text file Load
score_rdd = sc.textFile('/rdd/score.txt', 20)
```

# Transformation - Action

## RDD Transformation
-  데이터를 가공하기 위한 논리적 실행계획
-  기존의 RDD에 연산이 반영된 새로운 RDD를 반환한다.

## Transformation 메서드

1. filter()
2. map()
3. flatMap()
4. distinct()
5. zip()
6. join()
6. reduceByKey()
7. mapValues()
8. sortBy()

### Transformation - filter()
```python
score_rdd = sc.textFile('/rdd/score.txt')

# filter()
# 조건에 맞는 데이터만
score_rdd.filter(lambda e : '스파크' in e).filter(lambda e : '홍길' in e).collect()
type(score_rdd.filter(lambda e : '스파크' in e))
```

### Transformation - map()
```python
# map()
# 각각의 요소에 적용
data = [1, 3, 4, 7, 9]
map_rdd = sc.parallelize(data)
map_rdd.map(lambda e : e * 2).collect()
```

### Transformation - flatMap()
```python
# FlatMap()
# 각각의 요소에 함수를 적용한 다음 평면화 시켜주는 함수
nlist = [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9]]

flat_rdd = sc.parallelize(nlist)

def append_data(e) :
    e.append(100)
    return e

res = flat_rdd.flatMap(lambda e : append_data(e)).collect()
len(res)
# [[1, 2, 3, 100], [4, 5, 6, 100], [7, 8, 9, 100]]
res
```

### Transformation - distinct()
```python
# 중복 제거
nlist = [1, 2, 3, 1, 2, 3, 1, 2, 3 , 4, 5]
distinct_rdd = sc.parallelize(nlist)
distinct_rdd.distinct().collect()

slist = ['안녕','반가워','hello','hello']
distinct_rdd2 = sc.parallelize(slist)
distinct_rdd2.distinct().collect()
```

### Transformation - zip()
```python
# zip : 두 RDD를 결합해 key - value 형태의 RDD(Pair RDD)로 생성
foods = ['파스타','스테이크', '불고기', '비빔밥', '김치']
category = ['양식', '양식', '한식', '한식', '한식']

foods_rdd = sc.parallelize(foods)
category_rdd = sc.parallelize(category)

zip_rdd = category_rdd.zip(foods_rdd)
zip_rdd
zip_rdd.collect()

# 2
tmp = list(map(lambda a, b : (a, b), category, foods))
tmp_rdd = sc.parallelize(tmp)
tmp_rdd.collect()

tmp = list((zip(category, foods)))
tmp
```

### Transformation - reduceByKey(), mapValues()
```python
# redusceByKey : 키 값을 기준으로  value 값들을 연산
# mapValues : Pair RDD의 value들에 대해 map 연산을 수행
res = zip_rdd.reduceByKey(lambda a, b : a + ',' + b).mapValues(lambda a : a.split(','))
res.collect()
```

### Transformation - sortBy()
```python
# 키값으로 내림차순
res.sortBy(lambda e : e[0], ascending = False).collect()

# value 값으로 오름차순
# 메뉴 가짓 수로 오름차순
res.sortBy(lambda e : len(e[1][1]), ascending = False).collect()
```