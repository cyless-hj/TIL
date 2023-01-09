```python
Stack = []
SIZE = 5
Top = -1

def isEmpty():
    global Stack, SIZE, Top
    if Top == -1:
        return True
    else:
        return False

def isFull():
    global Stack, SIZE, Top
    if Top >= SIZE - 1:
        return True
    else:
        return False

def push(data):
    global Stack, SIZE, Top
    if isFull():
        print('스택이 꽉 찼습니다.')
        return
    else:
        Top += 1
        Stack[Top] = data

def pop():
    global Stack, SIZE, Top
    if isEmpty():
        print('스택이 비었습니다.')
        return
    else:
        data = Stack[Top]
        Stack[Top] = None
        Top -= 1
        return data

def peek(): # top 위치 데이터 확인
    global Stack, SIZE, Top
    if isEmpty():
        print('스택이 비었습니다.')
        return None
    else:
        return Stack[Top]
        
```