from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_points(maps):
    col, row = len(maps), len(maps[0])
    
    for i in range(col) :
        for j in range(row) :
            if maps[i][j] == 'S' :
                start = (j, i)
            if maps[i][j] == 'L' :
                lever = (j, i)
    
    return start, lever

def bfs(start, maps, target) :
    col, row = len(maps), len(maps[0])
    x, y = start
    visited = [[False]*row for _ in range(col)]
    visited[y][x] = True
    q = deque([(x, y, 0)])

    while q :
        x, y, dist = q.popleft()
        if maps[y][x] == target :
            return dist
        
        for k in range(4) :
            ax, ay = x + dx[k], y + dy[k]
            if -1 < ax < row and -1 < ay < col and not visited[ay][ax] and maps[ay][ax] != 'X' :
                visited[ay][ax] = True
                q.append((ax, ay, dist+1))
        
    return -1

def solution(maps):    
    start, lever = find_points(maps)
    lever_dist = bfs(start, maps, 'L')
    end_dist = bfs(lever, maps, 'E')

    return lever_dist + end_dist if lever_dist > -1 and end_dist > -1 else -1