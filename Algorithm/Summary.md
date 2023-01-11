# 코테 대비 요약

## 진수 변환 (10 -> N)
```python
import string

def convert_recur(num, base):
    number = string.digits + string_ascii_uppercase
    # number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    q, r = divmod(num, base)
    return convert_recur(q, base) + number[r] if q else number[r]
```

## 진수 변환 (N -> N)
```python
# N진수 -> 10
print(int('111',2))
print(int('222',3))
print(int('333',4))
print(int('444',5))
print(int('555',6))
print(int('FFF',16))

# 10 -> N
import string

tmp = string.digits+string.ascii_uppercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]
```

## 소수 찾기
```python
num = set(range(2, n + 1))
for i in range(2, n + 1):
    if i in num:
        num -= set(range(2 * i, n + 1, i))
```

## 소수 판별
```python
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임
```

## 이진 탐색
- 시간 복잡도 : logN
- **정렬되어 있어야 한다.**
```python
def biSearch(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None
```
## 값이 특정 범위에 속하는 데이터 개수 구하기
```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 배열 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_bu_range(a, -1, 3))
```

## 팩토리얼(DP)
```python
arr = [0 for _ in range(11)]

for i in range(1, 11):
    if i == 1:
        arr[i] = 1
    else:
        arr[i] = arr[i - 1] * i
```

## 피보나치
```python
a, b = 0, 1
for i in range(n - 1):
    a, b = b, a + b
answer = b % 1234567
```

## 선택 정렬
- 시간 복잡도 : N^2
```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]
print(array)
```

## 삽입 정렬
- 시간 복잡도 : N^2
    - 최선 : N
``` python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)
```

## 계수 정렬
- 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
- 시간 복잡도 : 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행 시간 O(N + K)를 보장
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

cnt = [0] * (max(array) + 1)

for i in array:
    cnt[i] += 1

for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i, end=' ')
```

## 퀵 정렬
- 시간 복잡도 : O(NlogN)
    - 최악의 경우 : O(N^2)
```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return array
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
```

## 퀵 정렬(파이썬 최적화)
```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_arr = [x for x in tail if x <= pivot]
    right_arr = [x for x in tail if x > pivot]

    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)
quick_sort(array)
```

## DFS
- 시간 복잡도 : N
```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]
visited = [False] * 9

dfs(graph, 1, visited)
```

## BFS
- 시간 복잡도 : N
```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]
visited = [False] * 9

bfs(graph, 1, visited)
```