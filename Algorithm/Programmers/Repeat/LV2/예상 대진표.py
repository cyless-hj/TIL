def solution(n,a,b):
    answer = 0

    a, b = a - 1, b - 1
    while a // 2 != b // 2:
        a //= 2
        b //= 2
        answer += 1

    return answer + 1