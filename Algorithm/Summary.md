# 코테 대비 요약

## 진수 변환 (10 -> N)
```python
import string

def convert_recur(num, base):
    number = string.digits + string.ascii_uppercase
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

tmp = string.digits+string.ascii_lowercase
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