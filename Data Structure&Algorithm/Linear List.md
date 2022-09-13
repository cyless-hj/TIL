# 선형 리스트(Linear List)

## 개념
- 데이터를 일정한 순서로 나열한 자료구조
- 순차 리스트(Ordered List)라고도 함
- 선형 리스트는 입력 순서대로 저장하는 데이터에 적당

### 데이터 삽입
```python
## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()

def insertNode(findData, insertData) :
	global memory, head, current, pre

	if head.data == findData :      # 첫 번째 노드 삽입
		node = Node()
		node.data = insertData
		node.link = head
		head = node
		return

	current = head
	while current.link != None :    # 중간 노드 삽입
		pre = current
		current = current.link
		if current.data == findData :
			node = Node()
			node.data = insertData
			node.link = current
			pre.link = node
			return

	node = Node()                   # 마지막 노드 삽입
	node.data = insertData
	current.link = node

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node()			# 첫 번째 노드
	node.data = dataArray[0]
	head = node
	memory.append(node)

	for data in dataArray[1:] :		# 두 번째 노드부터
		pre = node
		node = Node()
		node.data = data
		pre.link = node
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
### 데이터 삭제
```python
## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()

def deleteNode(deleteData) :
	global memory, head, current, pre

	if head.data == deleteData :         # 첫 번째 노드 삭제
		current = head
		head = head.link
		del(current)
		return

	current = head                          # 첫 번째  외 노드 삭제
	while current.link != None :
		pre = current
		current = current.link
		if current.data == deleteData :
			pre.link = current.link
			del(current)
			return

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node()			# 첫 번째 노드
	node.data = dataArray[0]
	head = node
	memory.append(node)

	for data in dataArray[1:] :		# 두 번째 노드부터
		pre = node
		node = Node()
		node.data = data
		pre.link = node
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
### 데이터 탐색
```python
## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()

def findNode(findData) :
	global memory, head, current, pre

	current = head
	if current.data == findData :
		return current
	while current.link != None :
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

	node = Node()			# 첫 번째 노드
	node.data = dataArray[0]
	head = node
	memory.append(node)

	for data in dataArray[1:] :		# 두 번째 노드부터
		pre = node
		node = Node()
		node.data = data
		pre.link = node
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