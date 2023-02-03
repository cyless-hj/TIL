def solution(topping):
    answer = 0
    fwd = set()
    bwd = {}
    
    for i in topping:
        bwd[i] = bwd.get(i, 0) + 1

    for i in topping:
        fwd.add(i)
        bwd[i] -= 1
        if bwd[i] == 0:
            del bwd[i]
        if len(fwd) == len(bwd.keys()):
            answer += 1
    return answer