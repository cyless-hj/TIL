def solution(n, m, section):
    answer = 0
    start = section[0] - 1
    for sect in section:
        if start < sect:
            start = sect + m - 1
            answer += 1
    return answer