from collections import deque

def solution(maps):
    answer = []
    maps = [list(m) for m in maps]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x ,y):
        if maps[x][y] != 'X':
            cnt = [int(maps[x][y])]
        else:
            cnt = []
            
        queue = deque([(x, y)])
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                if maps[nx][ny] == 'X':
                    continue
                if maps[nx][ny] != 'X':
                    queue.append((nx, ny))
                    cnt.append(int(maps[nx][ny]))
                    maps[nx][ny] = 'X'
        if len(cnt) != 1:
            cnt = cnt[1:]
        
        return cnt

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X':
                b = bfs(i, j)
                if b != 0:
                    answer.append(sum(b))
    answer.sort()
    
    if len(answer) == 0:
        answer = [-1]
        
    return answer