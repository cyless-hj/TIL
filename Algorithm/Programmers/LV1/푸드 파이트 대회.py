def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    answer = answer + '0' + ''.join(sorted(answer, reverse=True))
    return answer