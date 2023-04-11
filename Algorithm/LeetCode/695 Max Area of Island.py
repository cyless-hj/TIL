from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        answer = 0
        n, m = len(grid), len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def bfs(x, y):
            queue = deque([(x, y)])
            cnt = 0
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if grid[nx][ny] == 0:
                        continue
                    if grid[nx][ny] == 1:
                        queue.append((nx, ny))
                        cnt += 1
                        grid[nx][ny] = 0
            return 1 if cnt == 0 else cnt

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count = bfs(i, j)
                    print(count)
                    if count > answer:
                        answer = count
        return answer