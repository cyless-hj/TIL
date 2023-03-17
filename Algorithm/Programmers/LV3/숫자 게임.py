def solution(A, B):
    answer = 0
    tmpA = sorted(A)
    tmpB = sorted(B)
    
    idxA, idxB = 0, 0
    
    for i in range(len(tmpA)):
        if tmpA[idxA] < tmpB[idxB]:
            answer += 1
            idxA += 1
            idxB += 1
        else:
            idxB += 1
    return answer