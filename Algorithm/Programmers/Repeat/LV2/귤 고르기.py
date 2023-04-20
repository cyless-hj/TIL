from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnt_list = Counter(tangerine).most_common()
    total = 0
    for cnt in cnt_list:
        answer += 1
        total += cnt[1]
        if total >= k:
            break
    return answer