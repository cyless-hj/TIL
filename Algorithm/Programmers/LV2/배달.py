def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    
    for a in range(N+1):
        graph[a][a] = 0
                
    for r in road:
        graph[r[0]][r[1]] = min(graph[r[0]][r[1]], r[2])
        graph[r[1]][r[0]] = min(graph[r[1]][r[0]], r[2])
                
    for x in range(1,N+1):
        for a in range(1,N+1):
            for b in range(1,N+1):
                graph[a][b] = min(graph[a][x]+graph[b][x], graph[a][b])
    for i in range(1, N + 1):
        if graph[1][i] <= K:
            answer += 1
    return answer
