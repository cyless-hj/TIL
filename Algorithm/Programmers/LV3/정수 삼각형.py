def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(len(triangle[i]) - 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + triangle[i][j])
            dp[i][j + 1] = max(dp[i][j + 1], dp[i - 1][j] + triangle[i][j + 1])

    answer = max(dp[-1])
    return answer