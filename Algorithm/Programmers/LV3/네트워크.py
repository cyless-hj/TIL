def solution(n, computers):
    answer = 0
    def dfs(x):
        if computers[x][x] == 0:
            return
        else:
            computers[x][x] = 0
            neighbors = [i for i in range(n) if computers[x][i] == 1]
            for neighbor in neighbors:
                computers[x][neighbor], computers[neighbor][x] = 0, 0
                dfs(neighbor)

    for i in range(n):
        if computers[i][i] != 0:
            dfs(i)
            answer += 1
    return answer