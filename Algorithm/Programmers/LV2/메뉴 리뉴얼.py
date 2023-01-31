from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:
        candidates = []
        for o in orders:
            for li in combinations(o, c):
                res = ''.join(sorted(li))
                candidates.append(res)
        sorted_candidates = Counter(candidates).most_common()
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)