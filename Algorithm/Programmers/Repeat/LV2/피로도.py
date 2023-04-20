from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for perm in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0
        for pm in perm:
            if tmp >= pm[0]:
                tmp -= pm[1]
                cnt += 1
            if cnt > answer:
                answer = cnt
    return answer