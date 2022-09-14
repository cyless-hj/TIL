# 정렬(Sort)
- 순서대로 데이터가 나열되어 있는 것

## 개념
- 자료들을 일정한 순서대로 나열한 것

## 종류
- 오름차순 정렬이든 내림차순 정렬이든 결과의 형태만 다를 뿐이지 같은 방식으로 처리됨
- 정렬하는 방법에 대한 정렬 알고리즘은 수십 가지
    - 선택 정렬(Selection Sort) : 여러 데이터 중에서 가장 작은 값을 뽑는 작동을 반복하여 값을 정렬
    - 삽입 정렬(Insertion Sort) : 기존 데이터 중에서 자신의 위치를 찾아 데이터를 삽입하는 정렬
    - 버블 정렬(Bubble Sort)
    - 퀵 정렬(Quick Sort) 등등...

## 선택 정렬
```python
## 함수 선언 부분 ##
def selectionSort(ary) :
	n = len(ary)
	for i in range(0, n-1) :
		minIdx = i
		for k in range(i+1, n) :
			if (ary[minIdx] > ary[k]) :
				minIdx = k
		tmp = ary[i]
		ary[i] = ary[minIdx]
		ary[minIdx] = tmp

	return ary

## 전역 변수 선언 부분 ##
dataAry = [188, 162, 168, 120, 50, 150, 177, 105]

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry)

'''
정렬 전 --> [188, 162, 168, 120, 50, 150, 177, 105]
정렬 후 --> [50, 105, 120, 150, 162, 168, 177, 188]
'''
```

## 삽입 정렬

```python
## 함수 선언 부분 ##
def findInsertIdx(ary, data) :
	findIdx = -1			# 초깃값은 없는 위치로
	for i in range(0, len(ary)) :
		if (ary[i] > data ) :
			findIdx = i
			break
	if findIdx == -1 :			# 큰 값을 못찾음 == 제일 마지막 위치
		return len(ary)
	else :
		return findIdx

## 전역 변수 선언 부분 ##
before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

## 메인 코드 부분 ##
print('정렬 전 -->', before)
for i in range(len(before)) :
	data = before[i]
	insPos = findInsertIdx(after, data)
	after.insert(insPos, data)
print('정렬 후 -->', after)

'''
정렬 전 --> [188, 162, 168, 120, 50, 150, 177, 105]
정렬 후 --> [50, 105, 120, 150, 162, 168, 177, 188]
'''
```