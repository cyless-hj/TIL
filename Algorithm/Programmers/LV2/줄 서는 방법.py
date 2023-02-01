def factorial(n):
    dp = [0 for _ in range(n + 1)]
    for i in range(n + 1):
        if i == 0 or i == 1:
            dp[i] = 1
        else:
            dp[i] = dp[i - 1] * i
    return dp

def solution(n, k):
    answer = []
    num_list = list(range(1, n + 1))
    factorial_arr = factorial(n)
    for i in range(n - 1, 0, -1):
        q = k // factorial_arr[i]
        if k % factorial_arr[i] != 0:
            q += 1
        answer.append(num_list[q - 1])
        del num_list[q - 1]
        k %= factorial_arr[i]
    answer.append(num_list[0])
    return answer
