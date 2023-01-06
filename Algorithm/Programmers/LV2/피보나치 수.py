def solution(n):
    answer = 0
    a, b = 0, 1
    for i in range(n - 1): # 0, 1번째는 초기에 잡아줬기에 n - 1 까지
        a, b = b, a + b
    answer = b % 1234567
    return answer
# 재귀로 푸니 시간 초과