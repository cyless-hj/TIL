from itertools import combinations

def solution(nums):
    answer = 0

    arr = list(combinations(nums, 3))
    for i in arr:
        s = sum(i)
        tmp = 0
        for j in range(1, s + 1):
            if s % j == 0:
                tmp += 1
        if tmp == 2:
            answer += 1

    return answer