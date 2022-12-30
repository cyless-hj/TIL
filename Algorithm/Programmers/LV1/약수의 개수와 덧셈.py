def solution(left, right):
    answer = 0
    
    for j in range(left, right + 1):
        num = []
        for i in range(1, j + 1):
            if j % i == 0:
                num.append(i)
        if len(num) % 2 == 0:
            answer += j
        else:
            answer -= j
    return answer