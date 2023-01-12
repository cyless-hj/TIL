import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 1
visited = [0 for _ in range(n + 1)]

def bfs(start):
    global cnt
    queue = deque([start])
    visited[start] = cnt
    while queue:
        v = queue.popleft()
        graph[v].sort()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                cnt += 1
                visited[i] = cnt
                
bfs(r)
for i in range(1, n + 1):
    print(visited[i])