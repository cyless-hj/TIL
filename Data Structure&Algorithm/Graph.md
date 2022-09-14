# 그래프(Graph)

## 개념
- 여러 노드가 서로 연결된 자료구조

## 종류
- 무방향 그래프
    - 간선에 방향성이 없는 그래프
- 방향 그래프
    - 화살표로 간선 방향을 표기하고, 그래프의 정점 집합이 무방향 그래프와 같음
- 가중치 그래프
    - 간선마다 가중치가 다르게 부여된 그래프

## 깊이 우선 탐색의 작동
- 그래프의 모든 정점을 한 번씩 방문하는 것을 그래프 순회(Graph Traversal)라고 함
- 그래프 순회 방식은 깊이 우선 탐색, 너비 우선 탐색이 대표적

## 그래프의 인접 행렬 표현
- 그래프를 코드로 구현할 때는 인접 행렬을 사용
- 인접 행렬은 정방형으로 구성된 행렬로 정점이 4개인 그래프는 4×4로 표현

```python
## 함수 선언 부분 ##
class Graph() :
	def __init__ (self, size) :
		self.SIZE = size
		self.graph = [ [0 for _ in range(size)] for _ in range(size) ]

## 전역 변수 선언 부분 ##
G1, G3 = None, None

## 메인 코드 부분 ##
G1 = Graph(4)
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print('## G1 무방향 그래프 ##')
for row in range(4) :
	for col in range(4) :
		print(G1.graph[row][col], end=' ')
	print()

G3 = Graph(4)
G3.graph[0][1] = 1; G3.graph[0][2] = 1
G3.graph[3][0] = 1; G3.graph[3][2] = 1

print('## G3 방향 그래프 ##')
for row in range(4) :
	for col in range(4) :
		print(G3.graph[row][col], end=' ')
	print()
```