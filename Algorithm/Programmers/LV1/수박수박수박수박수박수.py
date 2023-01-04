def solution(n):
    answer = ''
    for i in range(1, n + 1):
        if i % 2 == 0:
            s = '박'
        else:
            s = '수'
        answer += s
    return answer