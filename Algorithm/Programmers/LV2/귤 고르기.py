from collections import Counter

def solution(k, tangerine):
    answer = 0
    c_tan = Counter(tangerine).most_common()
    
    cnt = 0
    i = 0
    while True:
        cnt += c_tan[i][1]
        if cnt >= k:
            break
        else:
            i += 1
    return i + 1