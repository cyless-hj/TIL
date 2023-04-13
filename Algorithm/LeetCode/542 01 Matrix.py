from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # answer = []
        # m, n = len(mat), len(mat[0])
        # dx = [-1, 1, 0, 0]
        # dy = [0, 0, -1, 1]
        # def bfs(a, b):
        #     queue = deque([(a, b)])
        #     while queue:
        #         x, y = queue.popleft()
        #         if mat[x][y] == 0:
        #             return 0
        #         for i in range(4):
        #             nx = x + dx[i]
        #             ny = y + dy[i]
        #             if nx < 0 or nx >= m or ny < 0 or ny >= n:
        #                 continue
        #             if mat[nx][ny] == 0:
        #                 return abs(a - nx) + abs(b - ny)
        #             if mat[nx][ny] == 1:
        #                 queue.append((nx, ny))
        # for i in range(m):
        #     tmp = []
        #     for j in range(n):
        #         tmp.append(bfs(i, j))
        #     answer.append(tmp)
        # return answer
        row = len(mat)
        col = len(mat[0])
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        dq = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0 :
                    dq.append((i,j))
                else : 
                    mat[i][j] = 987654321
        while dq : 
            x,y = dq.popleft()
            for k in range(4):
                newx,newy = x + dx[k] , y + dy[k]
                z = mat[x][y]+1 
                if 0 <= newx and newx < row and 0 <= newy and newy < col and mat[newx][newy] > z :
                    mat[newx][newy] = z
                    dq.append((newx,newy))
        return mat