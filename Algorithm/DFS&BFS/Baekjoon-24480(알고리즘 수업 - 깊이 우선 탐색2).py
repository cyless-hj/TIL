import sys
sys.setrecursionlimit(10**9)

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
cnt = 1

def dfs(v):
    global cnt
    visited[v] = cnt
    graph[v].sort(reverse=True)
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)
dfs(r)
for i in range(1, n + 1):
    print(visited[i])