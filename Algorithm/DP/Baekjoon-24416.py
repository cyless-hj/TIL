import sys

dp = [0] * 50
dp[1] = dp[2] = 1

n = int(sys.stdin.readline())

def fibonacci(n):
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

count1 = fibonacci(n)
count2 = n-2

print(count1, count2)