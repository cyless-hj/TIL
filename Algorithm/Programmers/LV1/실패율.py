def solution(N, stages):
    answer = {}
    tmp = len(stages)

    for stage in range(1, N + 1):
        if tmp != 0:
            count = stages.count(stage)
            answer[stage] = count / tmp
            tmp -= count               
        else:
            answer[stage] = 0
    
    return sorted(answer, key=lambda x: answer[x], reverse=True)