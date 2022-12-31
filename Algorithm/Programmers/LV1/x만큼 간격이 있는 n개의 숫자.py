def solution(x, n):
    answer = []
    tmp = x
    while len(answer) < n:
        answer.append(tmp)
        tmp += x
    return answer