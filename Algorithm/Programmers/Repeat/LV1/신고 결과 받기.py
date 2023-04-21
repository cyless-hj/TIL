from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    user = defaultdict(set)
    cnt = defaultdict(int)
    for name in report:
        a, b = name.split()
        user[a].add(b)
        cnt[b] += 1
    
    for i in id_list:
        tmp = 0
        for j in user[i]:
            if cnt[j] >= k:
                tmp += 1
        answer.append(tmp)
    return answer