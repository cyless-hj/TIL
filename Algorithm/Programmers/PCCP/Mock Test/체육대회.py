from itertools import permutations

def solution(ability):
    answer = 0
    p = list(permutations(ability, len(ability[0])))
    for i in range(len(p)):
        total = 0
        for j in range(len(p[i])):
            total += p[i][j][j]
        answer = max(answer, total)
    return answer