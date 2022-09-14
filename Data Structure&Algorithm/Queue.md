# 큐(Queue)
- 먼저 들어간 것이 먼저 나오는 구조
- 입구와 출구가 따로 있는 원통 형태

## 큐 원리
- 구조와 용어
    - 큐에 데이터를 삽입하는 작동 : enQueue(인큐)
    - 데이터를 추출하는 작동 : deQueue(데큐)
    - 저장된 데이터 중 첫 번째 데이터 : front(머리)
    - 저장된 데이터 중 마지막 데이터 : rear(꼬리)

```python
## 함수 선언 부분 ##
def isQueueFull() :
	global SIZE, queue, front, rear
	if (rear == SIZE-1) :
		return True
	else :
		return False

def isQueueEmpty() :
	global SIZE, queue, front, rear
	if (front == rear) :
		return True
	else :
		return False

def enQueue(data) :
	global SIZE, queue, front, rear
	if (isQueueFull()) :
		print("큐가 꽉 찼습니다.")
		return
	rear += 1
	queue[rear] = data

def deQueue() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("큐가 비었습니다.")
		return None
	front += 1
	data = queue[front]
	queue[front] = None
	return data

def peek() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("큐가 비었습니다.")
		return None
	return queue[front+1]

## 전역 변수 선언 부분 ##
SIZE = int(input("큐의 크기를 입력하세요 ==> "))
queue = [ None for _ in range(SIZE) ]
front = rear = -1

## 메인 코드 부분 ##
if __name__ == "__main__" :
	select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

	while (select != 'X' and select != 'x') :
		if select=='I' or select =='i' :
			data = input("입력할 데이터 ==> ")
			enQueue(data)
			print("큐 상태 : ", queue)
		elif select=='E' or select =='e' :
			data = deQueue()
			print("추출된 데이터 ==> ", data)
			print("큐 상태 : ", queue)
		elif select=='V' or select =='v' :
			data = peek()
			print("확인된 데이터 ==> ", data)
			print("큐 상태 : ", queue)
		else :
			print("입력이 잘못됨")

		select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

	print("프로그램 종료!")
```

## 원형 큐

### 개념
- 큐의 처음과 끝이 연결된 구조
- 순차 큐를 구부려서 끝을 이은 원형 큐
    - 오버헤드가 발생하지 않음
- 원형 큐가 빈 경우와 꽉 찬 경우
    - rear+1과 front가 같은 경우에 원형 큐가 꽉 찬 것으로 처리

```python
## 함수 선언 부분 ##
def isQueueFull() :
	global SIZE, queue, front, rear
	if ( (rear + 1) % SIZE == front) :
		return True
	else :
		return False

def isQueueEmpty() :
	global SIZE, queue, front, rear
	if (front == rear) :
		return True
	else :
		return False

def enQueue(data) :
	global SIZE, queue, front, rear
	if (isQueueFull()) :
		print("큐가 꽉 찼습니다.")
		return
	rear = (rear + 1) % SIZE
	queue[rear] = data

def deQueue() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("큐가 비었습니다.")
		return None
	front = (front + 1) % SIZE
	data = queue[front]
	queue[front] = None
	return data

def peek() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("큐가 비었습니다.")
		return None
	return queue[(front + 1) % SIZE]

## 전역 변수 선언 부분 ##
SIZE = int(input("큐의 크기를 입력하세요 ==> "))
queue = [ None for _ in range(SIZE) ]
front = rear = 0

## 메인 코드 부분 ##
if __name__ == "__main__" :
	select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

	while (select != 'X' and select != 'x') :
		if select=='I' or select =='i' :
			data = input("입력할 데이터 ==> ")
			enQueue(data)
			print("큐 상태 : ", queue)
			print("front : ", front, ", rear : ", rear)
		elif select=='E' or select =='e' :
			data = deQueue()
			print("추출된 데이터 ==> ", data)
			print("큐 상태 : ", queue)
			print("front : ", front, ", rear : ", rear)
		elif select=='V' or select =='v' :
			data = peek()
			print("확인된 데이터 ==> ", data)
			print("큐 상태 : ", queue)
			print("front : ", front, ", rear : ", rear)
		else :
			print("입력이 잘못됨")

		select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

	print("프로그램 종료!")
```