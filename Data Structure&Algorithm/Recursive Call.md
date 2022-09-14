# 재귀 호출
- 동일한 작동을 무한적으로 반복하는 알고리즘

## 개념
- 재귀 호출(Recursion)은 자신을 다시 호출하는 것

### 팩토리얼 구하기
```python
def factorial(n):
    if (n == 0 or n == 1) :
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
```

### 카운트다운
```python
def countDown(n):
    if n == 0 :
        print('발사!!')
    else :
        print(n)
        countDown(n - 1)

countDown(5)
```

### 별 모양 출력하기
```python
def printStar(n):
    if n > 0 :
        printStar(n - 1)
        print('*' * n)

printStar(5)
```