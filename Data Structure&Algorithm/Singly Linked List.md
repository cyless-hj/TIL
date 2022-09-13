# 단순 연결 리스트(Singly Linked List)
- 떨어진 곳에 위치한 데이터를 화살표로 연결한 것

## 개념
- 노드들이 물리적으로 떨어진 곳에 위치
- 각 노드의 번지도 순차적이지 않음
- 화살표로 표시된 연결(링크, Link)을 따라가면 선형 리스트 순서와 같음
- 데이터를 삽입/삭제할 때
    - 선형 리스트는 많은 작업이 필요(오버헤드 발생)
    - 단순 연결 리스트는 해당 노드의 앞뒤 링크만 수정하면 되므로 오버헤드가 거의 발생하지 않음

## 원리
- 노드 구조
    - 단순 연결 리스트는 다음 데이터를 가리키는 링크가 더 필요
    - 노드(Node)는 데이터와 링크로 구성된 항목

## 노드 삽입
```python
## 클래스와 함수 선언 부분 ##
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def printNodes(start):
	current = start
	if current.link == None :
		return
	print(current.data, end=' ')
	while current.link != start:
		current = current.link
		print(current.data, end=' ')
	print()

def insertNode(findData, insertData) :
	global memory, head, current, pre

	if head.data == findData :		# 첫 번째 노드 삽입
		node = Node()
		node.data = insertData
		node.link = head
		last = head		# 마지막 노드를 첫 번째 노드로 우선 지정
		while last.link != head :	# 마지막 노드를 찾으면 반복 종료
			last = last.link	# last를 다음 노드로 변경
		last.link = node		# 마지막 노드의 링크에 새 노드 지정
		head = node
		return

	current = head
	while current.link != head :		# 중간 노드 삽입
		pre = current
		current = current.link
		if current.data == findData :
			node = Node()
			node.data = insertData
			node.link = current
			pre.link = node
			return

	node = Node()			 # 마지막 노드 삽입
	node.data = insertData
	current.link = node
	node.link = head

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node()
	node.data = dataArray[0]	# 첫 번째 노드
	head = node
	node.link = head
	memory.append(node)

	for data in dataArray[1:] :	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		node.link = head
		memory.append(node)

	printNodes(head)

	insertNode("다현", "화사")
	printNodes(head)

	insertNode("사나", "솔라")
	printNodes(head)

	insertNode("재남", "문별")
	printNodes(head)

'''
다현 정연 쯔위 사나 지효 
화사 다현 정연 쯔위 사나 지효 
화사 다현 정연 쯔위 솔라 사나 지효 
화사 다현 정연 쯔위 솔라 사나 지효 문별 
'''
```

## 노드 삭제
```python
## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start):
	current = start
	if current.link == None :
		return
	print(current.data, end=' ')
	while current.link != start:
		current = current.link
		print(current.data, end=' ')
	print()

def deleteNode(deleteData) :
	global memory, head, current, pre

	if head.data == deleteData :		# 첫 번째 노드 삭제
		current = head
		head = head.link
		last = head
		while last.link != current:		# 마지막 노드를 찾으면 반복 종료
			last = last.link		# last를 다음 노드로 변경
		last.link = head			# 마지막 노드의 링크에 head가 가리키는 노드 지정
		del(current)
		return

	current = head	                        	# 첫 번째 외 노드 삭제
	while current.link != head :
		pre = current
		current = current.link
		if current.data == deleteData :  	# 중간 노드를 찾았을 때
			pre.link = current.link
			del(current)
			return

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node()		# 첫 번째 노드
	node.data = dataArray[0]
	head = node
	node.link = head
	memory.append(node)

	for data in dataArray[1:] :	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		node.link = head
		memory.append(node)

	printNodes(head)

	deleteNode("다현")
	printNodes(head)

	deleteNode("쯔위")
	printNodes(head)

	deleteNode("지효")
	printNodes(head)

	deleteNode("재남")
	printNodes(head)

'''
다현 정연 쯔위 사나 지효 
정연 쯔위 사나 지효 
정연 사나 지효 
정연 사나 
정연 사나 
'''
```

## 노드 탐색
```python
## 클래스와 함수 선언 부분 ##
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def printNodes(start):
	current = start
	if current.link == None :
		return
	print(current.data, end=' ')
	while current.link != start:
		current = current.link
		print(current.data, end=' ')
	print()

def findNode(findData) :
	global memory, head, current, pre

	current = head
	if current.data == findData :
		return current
	while current.link != head :
		current = current.link
		if current.data == findData :
			return current
	return Node()	# 빈 노드 반환

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node()		# 첫 번째 노드
	node.data = dataArray[0]
	head = node
	node.link = head
	memory.append(node)

	for data in dataArray[1:] :	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		node.link = head
		memory.append(node)

	printNodes(head)

	fNode = findNode("다현")
	print(fNode.data)

	fNode = findNode("쯔위")
	print(fNode.data)

	fNode = findNode("재남")
	print(fNode.data)

'''
다현 정연 쯔위 사나 지효 
다현
쯔위
None
'''
```