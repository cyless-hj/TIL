def solution(routes):
    answer = 1
    tmp = 30001
    routes.sort(key= lambda x: x[0])
    
    for i, j in routes:
        if i > tmp:
            answer += 1
            tmp = j
        tmp = min(j, tmp)
    return answer
