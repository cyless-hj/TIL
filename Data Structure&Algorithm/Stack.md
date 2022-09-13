# 스택(Stack)

## 개념
- 스택(Stack) 자료구조는 한쪽 끝이 막힌 형태(ex : 한쪽 끝이 막힌 주차장, 종이컵 수거함 등)
- 입구가 하나이기 때문에 먼저 들어간 것이 가장 나중에 나오는 구조(선입후출, 후입선출)

## 원리
- 스택 기본 구조
    - 스택에 데이터를 삽입하는 작동 : push
    - 스택에 데이터를 추출하는 작동 : pop
    - 스택에 들어 있는 가장 위의 데이터 : top

## 데이터 삽입 : push
```python
def isStackFull() :
	global SIZE, stack, top
	if (top >= SIZE-1) :
		return True
	else :
		return False

def push(data) :
	global SIZE, stack, top
	if (isStackFull()) :
		print("스택이 꽉 찼습니다.")
		return
	top += 1
	stack[top] = data

SIZE = 5
stack = ["커피", "녹차", "꿀물", "콜라", None]
top = 3

print(stack)
push("환타")
print(stack)
push("게토레이")

'''
['커피', '녹차', '꿀물', '콜라', None]
['커피', '녹차', '꿀물', '콜라', '환타']
스택이 꽉 찼습니다.
'''
```

## 데이터 추출 : pop
```python
def isStackEmpty() :
	global SIZE, stack, top
	if (top == -1) :
		return True
	else :
		return False

def pop() :
	global SIZE, stack, top
	if (isStackEmpty()) :
		print("스택이 비었습니다.")
		return None
	data = stack[top]
	stack[top] = None
	top -= 1
	return data

SIZE = 5
stack = ["커피", None, None, None, None]
top = 0

print(stack)
retData = pop()
print("추출한 데이터 -->", retData)
print(stack)
retData = pop()

'''
['커피', None, None, None, None]
추출한 데이터 --> 커피
[None, None, None, None, None]
스택이 비었습니다.
'''
```

## 데이터 확인 : peak
- top 위치의 데이터를 확인만 하고 스택에 그대로 두는 것

```python
def isStackEmpty() :
	global SIZE, stack, top
	if (top == -1) :
		return True
	else :
		return False

def peek() :
	global SIZE, stack, top
	if (isStackEmpty()) :
		print("스택이 비었습니다.")
		return None
	return stack[top]

SIZE = 5
stack = ["커피", "녹차", "꿀물", None, None]
top = 2

print(stack)
retData = peek()
print("top의 데이터 확인 -->", retData)
print(stack)

'''
['커피', '녹차', '꿀물', None, None]
top의 데이터 확인 --> 꿀물
['커피', '녹차', '꿀물', None, None]
'''
```