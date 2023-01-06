def solution(n):
    answer = 0
    a, b = 1, 2
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(1, n - 1):
            a, b = b, a + b
        answer = b % 1234567
        return answer
# 테스트 케이스를 생각하며 결과를 산출했을 때 피보나치인 것을 확인