def solution(n, m, section):
    answer = 0
    p = section[0] - 1
    for i in section:
        if p < i:
            p = i + m - 1
            answer += 1
    return answer