def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        try:
            s =  score[i : i + m]
            answer += score[i + m - 1] * m
        except:
            pass
    return answer