import sys

dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1

t = int(sys.stdin.readline())

for i in range(4, 101):
    dp[i] = dp[i - 3] + dp[i - 2]

for i in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])