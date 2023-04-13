class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        xSize = len(grid)
        ySize = len(grid[0])
        cnt = 0

        while True:
            temp = copy.deepcopy(grid)
            leftOrange = 0
            rottenOrange = 0
            for i in range(xSize):
                for j in range(ySize):
                    if grid[i][j] == 1:
                        leftOrange += 1
                    elif grid[i][j] == 2:
                        mx = [-1, 0, 1, 0]
                        my = [0, -1, 0, 1]
                        for p in range(4):
                            tx = i + mx[p]
                            ty = j + my[p]
                            if tx < 0 or tx >= xSize or ty < 0 or ty >= ySize or grid[tx][ty] == 0 or grid[tx][ty] == 2 or temp[tx][ty] == 2: continue
                            temp[tx][ty] = 2
                            rottenOrange += 1

            if rottenOrange == 0 and leftOrange != 0:
                return -1
            elif rottenOrange == 0 and leftOrange == 0:
                return cnt

            cnt += 1

            print(temp)

            grid = copy.deepcopy(temp)