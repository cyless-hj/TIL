```python
SIZE = 5
queue = [None for _ in range(SIZE)]
front = -1
rear = -1

def isFull():
    global SIZE, queue, front, rear
    if rear == SIZE - 1:
        return True
    else:
        return False

def isEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isFull():
        print('큐가 꽉 찼습니다.')
        return
    rear += 1
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isEmpty():
        print('큐가 비었습니다.')
        return None
    else:
        front += 1
        data = queue[front]
        queue[front] = None
        return data
def peek():
    global SIZE, queue, front, rear
    if isEmpty():
        print('큐가 비었습니다.')
        return None
    else:
        return queue[front + 1]
```