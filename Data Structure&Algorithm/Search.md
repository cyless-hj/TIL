# 검색(Search)
- '검색’은 정렬된 상태에서 빠르게 원하는 것을 찾을 수 있음

## 개념
- 어떤 집합에서 원하는 것을 찾는 것으로, 탐색이라고도 함
- 검색에는 순차 검색, 이진 검색, 트리 검색 등이 있음
- 검색에 실패하면 -1을 반환하는 것이 일반적임

## 종류
- 순차 검색
    - 검색할 집합이 정렬되어 있지 않은 상태일 때
    - 처음부터 차례대로 찾아보는 것으로, 쉽지만 비효율적임
    - 집합의 데이터가 정렬되어 있지 않다면 이 검색 외에 특별한 방법 없음
- 이진 검색
    - 데이터가 정렬되어 있다면 이진 검색도 사용 가능
    - 순차 검색에 비해 월등히 효율적이라 데이터가 몇 천만 개 이상이어도 빠르게 찾아낼 수 있음
- 트리 검색
    - 데이터 검색에는 상당히 효율적이지만 트리의 삽입, 삭제 등에는 부담

## 순차 검색
- 정렬되지 않은 집합의 순차 검색 원리와 구현

```python
## 함수 선언 부분 ## 
def seqSearch(ary, fData) :
	pos = -1
	size = len(ary)
	print('## 비교한 데이터 ==> ', end = '')
	for i in range(size) :
		print(ary[i], end = ' ')
		if ary[i] == fData :
			pos = i
			break
		elif ary[i] > fData :
			break
	print()
	return pos

## 전역 변수 선언 부분 ## 
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]
findData = 0

## 메인 코드 부분 ## 
dataAry.sort()
findData = int(input('* 찾을 값을 입력하세요. --> '))
print('배열 -->', dataAry)
position = seqSearch(dataAry, findData)
if position == -1 :
	print(findData, '(이)가 없네요.')
else :
	print(findData, '(은)는 ', position, '위치에 있음')

'''
* 찾을 값을 입력하세요. --> 150
배열 --> [50, 105, 120, 150, 162, 168, 177, 188]
## 비교한 데이터 ==> 50 105 120 150 
150 (은)는  3 위치에 있음
'''
```

## 이진 검색
- 이진 검색의 원리와 시간 복잡도
    - 이진 검색은 전체를 반씩 잘라 내서 한쪽을 버리는 방식을 사용

```python
## 함수 선언 부분 ## 
def binSearch(ary, fData) :
	pos = -1
	start = 0
	end = len(ary) - 1

	while (start <= end) :
		mid = (start + end ) // 2
		if fData == ary[mid] :
			return mid
		elif fData > ary[mid] :
			start = mid + 1
		else :
			end = mid - 1

	return pos

## 전역 변수 선언 부분 ##
dataAry = [ 50, 60, 105, 120, 150, 160, 162, 168, 177, 188]
findData = 162	# 할머니키

## 메인 코드 부분 ##
print('배열 -->', dataAry)
position = binSearch(dataAry, findData)
if position == -1 :
	print(findData,'(이)가 없네요.')
else :
	print(findData,'(은)는 ', position, '위치에 있음')

'''
배열 --> [50, 60, 105, 120, 150, 160, 162, 168, 177, 188]
162 (은)는  6 위치에 있음
'''
```