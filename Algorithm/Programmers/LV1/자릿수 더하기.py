def solution(n):
    answer = 0
    stn = str(n)
    for i in range(len(stn)):
        answer += int(stn[i])

    return answer