def solution(n):
    answer = []
    stn = str(n)
    for i in range(1, len(stn) + 1):
        answer.append(int(stn[-i]))
    return answer